# Auto Gemini Translator - Setup and Usage

## 🔧 Setup

### 1. Install dependencies
```bash
pip install requests
```

### 2. Get your Gemini API key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Copy the API key

## 🚀 Usage

### First: Check available models
```bash
python check_gemini_models.py --api-key YOUR_API_KEY
```

### Quick Test (first 3 batches)
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --test
```

### Translate all batches
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY
```

### Use specific model
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-pro
```

### Translate specific range
```bash
# Translate batches 1-10
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 1 --end 10

# Translate batches 50-117
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 50 --end 117
```

### Custom delay (to avoid rate limits)
```bash
# Wait 5 seconds between requests
python auto_gemini_translator.py --api-key YOUR_API_KEY --delay 5.0
```

## 📊 What it does

1. **Automatically processes** all 117 Vietnamese prompt files
2. **Calls Gemini API** for each batch with proper error handling
3. **Validates translations** and saves as CSV files
4. **Handles rate limiting** with automatic retries
5. **Provides progress tracking** and error reporting

## 📁 Output Files

- `vietnamese_translated_batch_001.csv` to `vietnamese_translated_batch_117.csv`
- Each file contains 50 Chinese→Vietnamese translations

## 🔄 Next Steps After Translation

### 1. Merge all translated files
```bash
python batch_splitter.py merge vietnamese_translated_batch_*.csv --output final_vietnamese.csv
```

### 2. Import to project
```bash
python chinese_text_extractor.py import --input final_vietnamese.csv --format csv
```

### 3. Validate results
```bash
python chinese_text_extractor.py validate
```

## ⚡ Features

- **Smart retry logic** with exponential backoff
- **Rate limit handling** (respects Gemini API limits)  
- **CSV validation** ensures translation quality
- **Progress tracking** shows completion status
- **Error recovery** logs failed batches for manual retry
- **Flexible batching** start/stop anywhere
- **Test mode** for trying first few batches

## 🛡️ Safety Features

- Low temperature (0.1) for consistent translations
- Content safety filters enabled
- Request timeout protection
- Automatic retry on failures
- CSV format validation

## 📈 Expected Performance

- **Processing time**: ~3-5 hours for all 117 batches
- **Rate limit**: ~1 request per 2 seconds (adjustable)
- **Success rate**: >95% with automatic retries
- **Cost**: Minimal (Gemini API is very affordable)

## 🔧 Troubleshooting

### Model not found error:
```bash
# First, check available models
python check_gemini_models.py --api-key YOUR_API_KEY

# Then use a supported model
python auto_gemini_translator.py --api-key YOUR_API_KEY --model gemini-1.5-flash
```

### If you get rate limit errors:
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --delay 10.0
```

### If some batches fail:
- Check the failed batch list in output
- Re-run with specific range:
```bash
python auto_gemini_translator.py --api-key YOUR_API_KEY --start 45 --end 50
```

### If API key is invalid:
- Make sure you copied the full API key
- Check if API key has proper permissions
- Verify your Google Cloud/AI Studio account

## 💡 Pro Tips

1. **Test first**: Always run `--test` mode first
2. **Monitor progress**: The tool shows real-time progress
3. **Check quality**: Review a few translated files manually
4. **Resume capability**: Can restart from any batch number
5. **Cost optimization**: Use `--delay` to control API usage

This automated tool will save you from manually copy-pasting 117 prompts to Gemini! 🎉