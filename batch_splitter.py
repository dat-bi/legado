#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch Splitter for AI Translation
Split large CSV files into manageable batches for AI translation services
"""

import csv
import math
import argparse
from pathlib import Path

def split_csv_into_batches(input_file, batch_size=50, output_prefix="batch"):
    """Split CSV file into smaller batches for AI translation."""
    
    input_path = Path(input_file)
    if not input_path.exists():
        print(f"Error: Input file {input_file} not found")
        return
    
    print(f"Reading {input_file}...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    if len(rows) < 2:
        print("Error: CSV file must have at least header + 1 data row")
        return
    
    header = rows[0]
    data_rows = rows[1:]
    
    num_batches = math.ceil(len(data_rows) / batch_size)
    
    print(f"Splitting {len(data_rows)} entries into {num_batches} batches of {batch_size} entries each...")
    
    batch_files = []
    
    for i in range(num_batches):
        start_idx = i * batch_size
        end_idx = min((i + 1) * batch_size, len(data_rows))
        batch_rows = data_rows[start_idx:end_idx]
        
        batch_filename = f"{output_prefix}_{i+1:03d}.csv"
        
        with open(batch_filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(batch_rows)
        
        batch_files.append(batch_filename)
        print(f"✓ Created {batch_filename} with {len(batch_rows)} entries")
    
    print(f"\nBatch splitting completed!")
    print(f"Created {len(batch_files)} batch files")
    return batch_files

def create_ai_prompt_file(batch_file, prompt_template="gemini"):
    """Create AI prompt file for a specific batch."""
    
    # Different prompt templates for different AI models
    templates = {
        "gemini": """Translate these Legado e-book app strings from Chinese to English.

**CONTEXT**: Legado is an Android e-book reader app with features like:
- Book sources management
- Reading interface customization  
- Text-to-speech (TTS)
- Import/Export functionality
- Web services

**REQUIREMENTS**:
- Natural English for mobile app users
- Keep CSV format exactly the same
- Fill in the "translation" column only
- Maintain placeholders like %s, %d, \\n
- Use consistent terminology

**COMMON TERMS**:
- 阅读 = Reading
- 书源 = Book Sources
- 书架 = Bookshelf  
- 朗读 = Read Aloud
- 设置 = Settings

CSV Data:
""",

        "chatgpt": """I need English translations for Chinese UI strings from the Legado Android e-book reader app.

**PROJECT CONTEXT**: Legado is a popular open-source Android app for reading e-books with advanced features like custom book sources, TTS, and web editing.

**TRANSLATION REQUIREMENTS**:
1. Natural, user-friendly English
2. Consistent with Android Material Design
3. Keep technical formatting unchanged (%s, %d, etc.)
4. Maintain CSV structure
5. Fill only the "translation" column

CSV to translate:
""",

        "claude": """Please translate these Chinese strings for the Legado e-book reader Android app.

**APP OVERVIEW**: Legado is an advanced e-book reader with book source management, customizable reading experience, and TTS features.

**STYLE GUIDE**:
- Mobile app UI language (concise, clear)
- Professional but user-friendly tone
- Consistent terminology across the app
- Follow Android conventions

**OUTPUT**: Return the same CSV with English translations in the "translation" column.

Data:
"""
    }
    
    prompt = templates.get(prompt_template, templates["gemini"])
    
    # Read the batch CSV content
    with open(batch_file, 'r', encoding='utf-8') as f:
        csv_content = f.read()
    
    # Create prompt file
    prompt_filename = f"ai_prompt_{Path(batch_file).stem}.txt"
    
    with open(prompt_filename, 'w', encoding='utf-8') as f:
        f.write(prompt + csv_content)
    
    print(f"✓ Created AI prompt: {prompt_filename}")
    return prompt_filename

def merge_translated_batches(batch_files, output_file="merged_translation.csv"):
    """Merge translated batch files back into one CSV."""
    
    all_rows = []
    header = None
    
    for batch_file in sorted(batch_files):
        if not Path(batch_file).exists():
            print(f"Warning: {batch_file} not found, skipping...")
            continue
            
        with open(batch_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
            
            if header is None:
                header = rows[0]
                all_rows.append(header)
            
            # Add data rows (skip header)
            all_rows.extend(rows[1:])
    
    # Write merged file
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(all_rows)
    
    print(f"✓ Merged {len(batch_files)} batches into {output_file}")
    print(f"Total entries: {len(all_rows) - 1}")  # -1 for header
    return output_file

def main():
    parser = argparse.ArgumentParser(description='Batch processing tool for AI translation')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Split command
    split_parser = subparsers.add_parser('split', help='Split CSV into batches')
    split_parser.add_argument('input_file', help='Input CSV file')
    split_parser.add_argument('--batch-size', type=int, default=50, help='Entries per batch (default: 50)')
    split_parser.add_argument('--prefix', default='batch', help='Output filename prefix (default: batch)')
    
    # Create prompt command
    prompt_parser = subparsers.add_parser('prompt', help='Create AI prompt files')
    prompt_parser.add_argument('batch_file', help='Batch CSV file')
    prompt_parser.add_argument('--template', choices=['gemini', 'chatgpt', 'claude'], 
                              default='gemini', help='AI model template (default: gemini)')
    
    # Merge command
    merge_parser = subparsers.add_parser('merge', help='Merge translated batches')
    merge_parser.add_argument('batch_files', nargs='+', help='Translated batch CSV files')
    merge_parser.add_argument('--output', default='merged_translation.csv', help='Output filename')
    
    # Auto command (split + create prompts)
    auto_parser = subparsers.add_parser('auto', help='Auto split and create prompts')
    auto_parser.add_argument('input_file', help='Input CSV file')
    auto_parser.add_argument('--batch-size', type=int, default=50, help='Entries per batch')
    auto_parser.add_argument('--template', choices=['gemini', 'chatgpt', 'claude'], 
                            default='gemini', help='AI model template')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'split':
        split_csv_into_batches(args.input_file, args.batch_size, args.prefix)
        
    elif args.command == 'prompt':
        create_ai_prompt_file(args.batch_file, args.template)
        
    elif args.command == 'merge':
        merge_translated_batches(args.batch_files, args.output)
        
    elif args.command == 'auto':
        print("🚀 Auto batch processing for AI translation")
        print("=" * 50)
        
        # Split into batches
        batch_files = split_csv_into_batches(args.input_file, args.batch_size)
        
        if batch_files:
            print(f"\nCreating AI prompt files using {args.template} template...")
            
            # Create prompt files for each batch
            for batch_file in batch_files:
                create_ai_prompt_file(batch_file, args.template)
            
            print(f"\n🎉 Ready for AI translation!")
            print(f"📁 Use the ai_prompt_*.txt files with your AI model")
            print(f"💡 After translation, save results as translated_batch_*.csv")
            print(f"🔄 Then run: python batch_splitter.py merge translated_batch_*.csv")

if __name__ == '__main__':
    main()