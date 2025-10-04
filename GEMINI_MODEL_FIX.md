# 🔧 Gemini Model Fix Guide

## ❌ The Problem

You're getting this error:
```
models/gemini-pro is not found for API version v1beta, or is not supported for generateContent
```

## ✅ The Solution

The Gemini API model names have changed. Here's how to fix it:

### Step 1: Check Available Models

```bash
python check_gemini_models.py --api-key YOUR_API_KEY
```

**Expected Output:**
```
🔍 Checking available Gemini models...

✅ Found 3 models that support generateContent:
================================================================================
1. gemini-1.5-flash
   Display Name: Gemini 1.5 Flash
   Description: Fast and versatile performance across a diverse variety of tasks...
   Methods: generateContent, countTokens

2. gemini-1.5-pro
   Display Name: Gemini 1.5 Pro  
   Description: Mid-size multimodal model that supports up to 2 million tokens...
   Methods: generateContent, countTokens

3. gemini-1.0-pro
   Display Name: Gemini 1.0 Pro
   Description: The best model for scaling across a wide range of tasks...
   Methods: generateContent, countTokens

💡 Recommended models for translation:
   python auto_gemini_translator.py --api-key YOUR_KEY --model gemini-1.5-flash
   python auto_gemini_translator.py --api-key YOUR_KEY --model gemini-1.5-pro
```

### Step 2: Use the Latest Models

#### Option 1: Test Gemini 2.5 models automatically
```bash
python test_gemini_2_5.py --api-key YOUR_API_KEY
```

#### Option 2: Use specific 2.5 models
```bash
# Try Gemini 2.0 Flash (latest experimental)
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.0-flash-exp --test

# Try other 2.5 variants
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.5-flash --test
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.5-pro --test
```

#### Option 3: Fallback to 1.5 models
```bash
# Fast and cost-effective
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-flash --test

# More accurate but slower
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-pro --test
```

## 🎯 Recommended Models for Translation (Updated 2024)

| Model | Version | Speed | Quality | Cost | Recommendation |
|-------|---------|-------|---------|------|----------------|
| **gemini-2.0-flash-exp** | 2.0 | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | 💰 | **🔥 Best overall** |
| **gemini-2.5-flash** | 2.5 | ⚡⚡⚡ | ⭐⭐⭐⭐ | 💰 | **Latest technology** |
| **gemini-2.5-pro** | 2.5 | ⚡⚡ | ⭐⭐⭐⭐⭐ | 💰💰 | **Highest quality** |
| **gemini-1.5-flash** | 1.5 | ⚡⚡⚡ | ⭐⭐⭐ | 💰 | Reliable fallback |
| **gemini-1.5-pro** | 1.5 | ⚡⚡ | ⭐⭐⭐⭐ | 💰💰 | Quality fallback |

## 📝 Quick Test

Test with the latest model:

```bash
# Test with Gemini 2.0 Flash (latest and recommended)
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-2.0-flash-exp --test

# Or auto-test multiple 2.5 models
python test_gemini_2_5.py --api-key YOUR_API_KEY
```

**Expected Success Output:**
```
🧪 Test mode: Processing only first 3 batches
🤖 Using model: gemini-1.5-flash
🚀 Starting automated Vietnamese translation
📁 Processing batches 1 to 3
📊 Total batches: 3
⏱ Delay between requests: 2.0 seconds

[1/3] ----------------------------------------
📝 Processing vietnamese_prompt_batch_001...
  Expected entries: 50
  Calling Gemini API (attempt 1/3)...
  ✓ API call successful
  ✓ Saved: vietnamese_translated_batch_001.csv
```

## 🚨 If You Still Get Errors

### Check your API key:
```bash
# Make sure your key is valid
python check_gemini_models.py --api-key YOUR_API_KEY
```

### Common issues:
- **Invalid API key**: Go to [Google AI Studio](https://aistudio.google.com/app/apikey) and create a new key
- **No permissions**: Make sure your Google account has access to Gemini API
- **Rate limits**: Add `--delay 5.0` to slow down requests

### Working commands:
```bash
# These should work with the updated tool:
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-flash --test
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-pro --test
```

## ✅ Updated Files

The following files have been updated to fix the model issue:
- ✅ `auto_gemini_translator.py` - Updated with correct model names
- ✅ `check_gemini_models.py` - New tool to check available models  
- ✅ `AUTO_TRANSLATOR_README.md` - Updated documentation
- ✅ `HUONG_DAN_AUTO_GEMINI.md` - Updated Vietnamese guide

**You can now run the auto translator with confidence!** 🚀