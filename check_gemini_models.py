#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gemini Model Checker - Find available models for your API key
"""

import requests
import argparse
import json

def check_available_models(api_key: str):
    """Check which Gemini models are available for your API key"""
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models?key={api_key}"
    
    try:
        print("🔍 Checking available Gemini models...")
        
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            
            if 'models' in result:
                generateContent_models = []
                other_models = []
                
                for model in result['models']:
                    name = model.get('name', '').replace('models/', '')
                    supported_methods = model.get('supportedGenerationMethods', [])
                    display_name = model.get('displayName', name)
                    description = model.get('description', 'No description')
                    
                    model_info = {
                        'name': name,
                        'display_name': display_name,
                        'description': description,
                        'methods': supported_methods
                    }
                    
                    if 'generateContent' in supported_methods:
                        generateContent_models.append(model_info)
                    else:
                        other_models.append(model_info)
                
                print(f"\n✅ Found {len(generateContent_models)} models that support generateContent:")
                print("=" * 80)
                
                for i, model in enumerate(generateContent_models, 1):
                    print(f"{i}. {model['name']}")
                    print(f"   Display Name: {model['display_name']}")
                    print(f"   Description: {model['description'][:100]}...")
                    print(f"   Methods: {', '.join(model['methods'])}")
                    print()
                
                if other_models:
                    print(f"\n📋 Other available models ({len(other_models)}):")
                    print("-" * 50)
                    for model in other_models:
                        print(f"• {model['name']} (Methods: {', '.join(model['methods'])})")
                
                print(f"\n💡 Recommended models for translation:")
                # Prioritize newer models (2.0/2.5 series)
                recommended = []
                
                # Look for Gemini 2.0+ models first
                for model in generateContent_models:
                    name_lower = model['name'].lower()
                    if any(x in name_lower for x in ['2.0', '2.5', 'flash-exp', 'pro-exp']):
                        recommended.append(model)
                
                # Then add 1.5 models as fallback
                if len(recommended) < 3:
                    for model in generateContent_models:
                        name_lower = model['name'].lower()
                        if any(x in name_lower for x in ['1.5-flash', '1.5-pro']) and model not in recommended:
                            recommended.append(model)
                
                # Show top recommendations
                if recommended:
                    for model in recommended[:3]:
                        print(f"   python auto_gemini_translator.py --api-key YOUR_KEY --model {model['name']}")
                else:
                    # Fallback to any available model
                    for model in generateContent_models[:3]:
                        print(f"   python auto_gemini_translator.py --api-key YOUR_KEY --model {model['name']}")
                
                return generateContent_models
                
            else:
                print("❌ No models found in response")
                return []
                
        elif response.status_code == 400:
            print("❌ Invalid API key or request format")
            print("Please check your API key at: https://aistudio.google.com/app/apikey")
            return []
            
        elif response.status_code == 403:
            print("❌ Access denied - API key may not have permission")
            print("Make sure your API key has access to Gemini models")
            return []
            
        else:
            print(f"❌ API Error {response.status_code}: {response.text}")
            return []
            
    except requests.exceptions.Timeout:
        print("❌ Request timeout - check your internet connection")
        return []
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return []

def main():
    parser = argparse.ArgumentParser(description='Check available Gemini models')
    parser.add_argument('--api-key', required=True, help='Your Gemini API key')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    
    args = parser.parse_args()
    
    models = check_available_models(args.api_key)
    
    if args.json and models:
        print(f"\n📄 JSON Output:")
        print(json.dumps([m['name'] for m in models], indent=2))

if __name__ == '__main__':
    main()