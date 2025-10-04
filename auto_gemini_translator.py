#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automated Gemini API Translator for Legado Vietnamese Translation
Automatic batch file translation to Vietnamese using Gemini API
"""

import os
import time
import json
import glob
import csv
import requests
from pathlib import Path
from typing import List, Optional
import argparse

class GeminiAutoTranslator:
    """Automated translator using Gemini API for Vietnamese translation"""
    
    def __init__(self, api_key: str, model: str = "gemini-2.0-flash-exp"):
        self.api_key = api_key
        self.model = model
        self.base_url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"
        self.list_models_url = "https://generativelanguage.googleapis.com/v1beta/models"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.translated_count = 0
        self.failed_batches = []
        
    def list_available_models(self) -> List[str]:
        """List all available Gemini models"""
        
        try:
            response = requests.get(
                f"{self.list_models_url}?key={self.api_key}",
                headers=self.headers,
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                models = []
                
                if 'models' in result:
                    for model in result['models']:
                        name = model.get('name', '').replace('models/', '')
                        supported_methods = model.get('supportedGenerationMethods', [])
                        
                        if 'generateContent' in supported_methods:
                            models.append(name)
                
                return models
            else:
                print(f"Error listing models: {response.status_code} - {response.text}")
                return []
                
        except Exception as e:
            print(f"Error listing models: {e}")
            return []
    
    def call_gemini_api(self, prompt: str, max_retries: int = 3) -> Optional[str]:
        """Call Gemini API with retry logic"""
        
        payload = {
            "contents": [{
                "parts": [{
                    "text": prompt
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,  # Low temperature for consistent translation
                "topK": 1,
                "topP": 1,
                "maxOutputTokens": 8192,
            },
            "safetySettings": [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH", 
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]
        }
        
        for attempt in range(max_retries):
            try:
                print(f"  Calling Gemini API (attempt {attempt + 1}/{max_retries})...")
                
                response = requests.post(
                    f"{self.base_url}?key={self.api_key}",
                    headers=self.headers,
                    json=payload,
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    
                    if 'candidates' in result and len(result['candidates']) > 0:
                        content = result['candidates'][0]['content']['parts'][0]['text']
                        print(f"  [OK] API call successful")
                        return content
                    else:
                        print(f"  [FAIL] No content in API response: {result}")
                        
                elif response.status_code == 429:  # Rate limit
                    wait_time = (attempt + 1) * 10
                    print(f"  Rate limit hit. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                    
                else:
                    print(f"  [FAIL] API error {response.status_code}: {response.text}")
                    
            except requests.exceptions.Timeout:
                print(f"  [FAIL] Request timeout on attempt {attempt + 1}")
                time.sleep(5)
                
            except Exception as e:
                print(f"  [FAIL] Error on attempt {attempt + 1}: {e}")
                time.sleep(2)
        
        print(f"  [FAIL] Failed after {max_retries} attempts")
        return None
    
    def extract_csv_from_response(self, response: str) -> Optional[str]:
        """Extract CSV content from Gemini response"""
        
        # Look for CSV block in markdown
        if "```csv" in response:
            start = response.find("```csv") + 6
            end = response.find("```", start)
            if end != -1:
                return response[start:end].strip()
        
        # Look for CSV block without markdown
        if "```" in response:
            start = response.find("```") + 3
            end = response.find("```", start)
            if end != -1:
                csv_content = response[start:end].strip()
                if csv_content.startswith("id,type,file_path"):
                    return csv_content
        
        # Look for direct CSV content (starts with header)
        lines = response.split('\n')
        csv_start = -1
        for i, line in enumerate(lines):
            if line.strip().startswith("id,type,file_path"):
                csv_start = i
                break
        
        if csv_start >= 0:
            # Find end of CSV (empty line or non-CSV content)
            csv_end = len(lines)
            for i in range(csv_start + 1, len(lines)):
                line = lines[i].strip()
                if not line or not (line.count(',') >= 8):  # CSV should have at least 9 columns
                    csv_end = i
                    break
            
            csv_content = '\n'.join(lines[csv_start:csv_end])
            return csv_content
        
        # If no clear CSV found, return the whole response and let user handle it
        print(f"  [WARNING] Could not extract clear CSV format. Response length: {len(response)}")
        return response
    
    def validate_csv_translation(self, csv_content: str, expected_entries: int) -> bool:
        """Validate the translated CSV content"""
        
        try:
            lines = csv_content.strip().split('\n')
            if len(lines) < 2:  # Need header + at least 1 data row
                return False
            
            # Check header
            header = lines[0]
            if not header.startswith("id,type,file_path"):
                return False
            
            # Check if we have expected number of entries (header + data rows)
            if len(lines) != expected_entries + 1:
                print(f"  [WARNING] Expected {expected_entries + 1} lines, got {len(lines)}")
                return False
            
            # Check if translations are present (not empty)
            reader = csv.reader(lines)
            next(reader)  # Skip header
            
            translation_count = 0
            for row in reader:
                if len(row) >= 7 and row[6].strip():  # translation column (index 6)
                    translation_count += 1
            
            if translation_count < expected_entries * 0.8:  # At least 80% should be translated
                print(f"  [WARNING] Only {translation_count}/{expected_entries} entries translated")
                return False
            
            return True
            
        except Exception as e:
            print(f"  [FAIL] CSV validation error: {e}")
            return False
    
    def translate_batch(self, batch_file: str) -> bool:
        """Translate a single batch file"""
        
        batch_name = Path(batch_file).stem
        print(f"\nProcessing {batch_name}...")
        
        # Read prompt file
        try:
            with open(batch_file, 'r', encoding='utf-8') as f:
                prompt = f.read()
        except Exception as e:
            print(f"  [FAIL] Error reading {batch_file}: {e}")
            return False
        
        # Count expected entries
        lines = prompt.split('\n')
        csv_lines = [line for line in lines if line.strip() and ',' in line and not line.startswith('id,type,file_path')]
        expected_entries = len(csv_lines)
        
        print(f"  Expected entries: {expected_entries}")
        
        # Call Gemini API
        response = self.call_gemini_api(prompt)
        if not response:
            self.failed_batches.append(batch_name)
            return False
        
        # Extract CSV content
        csv_content = self.extract_csv_from_response(response)
        if not csv_content:
            print(f"  [FAIL] Could not extract CSV from response")
            self.failed_batches.append(batch_name)
            return False
        
        # Validate translation
        if not self.validate_csv_translation(csv_content, expected_entries):
            print(f"  [WARNING] CSV validation failed, but saving anyway for manual review")
        
        # Save translated CSV
        output_file = f"vietnamese_translated_{batch_name}.csv"
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(csv_content)
            
            print(f"  [OK] Saved: {output_file}")
            self.translated_count += 1
            return True
            
        except Exception as e:
            print(f"  [FAIL] Error saving {output_file}: {e}")
            self.failed_batches.append(batch_name)
            return False
    
    def translate_all_batches(self, start_batch: int = 1, end_batch: int = None, delay: float = 2.0):
        """Translate all Vietnamese prompt batches"""
        
        # Find all Vietnamese prompt files
        prompt_files = sorted(glob.glob('vietnamese_prompt_batch_*.txt'))
        
        if not prompt_files:
            print("[FAIL] No Vietnamese prompt files found!")
            print("Run 'python create_vietnamese_prompts.py' first.")
            return
        
        if end_batch is None:
            end_batch = len(prompt_files)
        
        # Filter files based on range
        filtered_files = []
        for file in prompt_files:
            batch_num = int(Path(file).stem.split('_')[-1])
            if start_batch <= batch_num <= end_batch:
                filtered_files.append(file)
        
        print(f"Starting automated Vietnamese translation")
        print(f"Processing batches {start_batch} to {end_batch}")
        print(f"Total batches: {len(filtered_files)}")
        print(f"Delay between requests: {delay} seconds")
        print("=" * 60)
        
        # Process each batch
        start_time = time.time()
        
        for i, batch_file in enumerate(filtered_files, 1):
            print(f"\n[{i}/{len(filtered_files)}] {'-' * 40}")
            
            success = self.translate_batch(batch_file)
            
            # Add delay between requests to avoid rate limiting
            if i < len(filtered_files):  # Don't wait after the last batch
                print(f"  [WAITING] Waiting {delay} seconds before next batch...")
                time.sleep(delay)
        
        # Summary
        elapsed_time = time.time() - start_time
        print(f"\n{'=' * 60}")
        print(f"Translation completed!")
        print(f"Successfully translated: {self.translated_count} batches")
        print(f"Failed batches: {len(self.failed_batches)}")
        print(f"Total time: {elapsed_time / 60:.1f} minutes")
        
        if self.failed_batches:
            print(f"\nFailed batches to retry manually:")
            for batch in self.failed_batches:
                print(f"  - {batch}")
        
        # Show next steps
        if self.translated_count > 0:
            print(f"\nNext steps:")
            print(f"1. Review translated files: vietnamese_translated_batch_*.csv")
            print(f"2. Merge all translations:")
            print(f"   python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv")
            print(f"3. Import to project:")
            print(f"   python chinese_text_extractor.py import --input final_vietnamese.csv --format csv")

def main():
    parser = argparse.ArgumentParser(description='Automated Gemini API translator for Vietnamese')
    parser.add_argument('--api-key', required=True, help='Gemini API key')
    parser.add_argument('--model', default='gemini-2.0-flash-exp', help='Gemini model to use (default: gemini-2.0-flash-exp)')
    parser.add_argument('--list-models', action='store_true', help='List available models and exit')
    parser.add_argument('--start', type=int, default=1, help='Start batch number (default: 1)')
    parser.add_argument('--end', type=int, help='End batch number (default: all)')
    parser.add_argument('--delay', type=float, default=2.0, help='Delay between requests in seconds (default: 2.0)')
    parser.add_argument('--test', action='store_true', help='Test with only first 3 batches')
    
    args = parser.parse_args()
    
    # Create translator
    translator = GeminiAutoTranslator(args.api_key, args.model)
    
    # List models mode
    if args.list_models:
        print("[INFO] Listing available Gemini models...")
        models = translator.list_available_models()
        
        if models:
            print(f"\n[SUCCESS] Available models that support generateContent:")
            for i, model in enumerate(models, 1):
                print(f"  {i}. {model}")
            
            print(f"\n[TIP] To use a specific model:")
            print(f"   python auto_gemini_translator.py --api-key YOUR_KEY --model {models[0]}")
        else:
            print("[ERROR] Could not retrieve model list. Check your API key.")
        
        return
    
    # Test mode
    if args.test:
        args.start = 1
        args.end = 3
        print("Test mode: Processing only first 3 batches")
    
    print(f"Using model: {args.model}")
    
    # Start translation
    translator.translate_all_batches(
        start_batch=args.start,
        end_batch=args.end,
        delay=args.delay
    )

if __name__ == '__main__':
    main()