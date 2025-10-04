#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Gemini 2.5 models specifically
"""

import sys
import subprocess
import argparse

def test_model(api_key: str, model: str):
    """Test a specific Gemini model with a small translation batch"""
    
    print(f"Testing model: {model}")
    print("=" * 60)
    
    # Test command
    cmd = [
        "python", "auto_gemini_translator.py",
        "--api-key", api_key,
        "--model", model,
        "--test"
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"[OK] Model {model} works successfully!")
            print("\nOutput:")
            print(result.stdout)
            return True
        else:
            print(f"[FAIL] Model {model} failed!")
            print("\nError:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"Model {model} test timed out (5 minutes)")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing model {model}: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Test Gemini 2.5 models')
    parser.add_argument('--api-key', required=True, help='Your Gemini API key')
    parser.add_argument('--model', help='Specific model to test')
    
    args = parser.parse_args()
    
    # Common Gemini 2.5 model names to try
    models_to_test = [
        "gemini-2.0-flash-exp",
        "gemini-2.5-flash",
        "gemini-2.5-pro", 
        "gemini-exp-1206",
        "gemini-flash-2.5",
        "gemini-pro-2.5",
        "gemini-1.5-flash",  # Fallback
        "gemini-1.5-pro"    # Fallback
    ]
    
    if args.model:
        # Test specific model
        test_model(args.api_key, args.model)
    else:
        # Test all models
        print("Testing multiple Gemini models to find the best one...")
        print("=" * 60)
        
        working_models = []
        
        for model in models_to_test:
            print(f"\n[{models_to_test.index(model) + 1}/{len(models_to_test)}]")
            if test_model(args.api_key, model):
                working_models.append(model)
                print(f"[OK] {model} added to working models list")
            else:
                print(f"[FAIL] {model} failed or not available")
        
        print("\n" + "=" * 60)
        print("Test Results Summary:")
        
        if working_models:
            print(f"[OK] Found {len(working_models)} working models:")
            for i, model in enumerate(working_models, 1):
                print(f"  {i}. {model}")
            
            best_model = working_models[0]
            print(f"\nRecommended model: {best_model}")
            print(f"\nTo run full translation with best model:")
            print(f"   python auto_gemini_translator.py --api-key YOUR_KEY --model {best_model}")
            
        else:
            print("[FAIL] No working models found!")
            print("Try checking your API key:")
            print("   python check_gemini_models.py --api-key YOUR_KEY")

if __name__ == '__main__':
    main()