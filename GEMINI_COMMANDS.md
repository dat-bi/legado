# 🤖 Exact Commands for Gemini AI Translation

## 🚀 Quick Start with Gemini

### Step 1: Prepare Batches (50 entries at a time for best results)

```bash
# Split your extraction into manageable batches
python batch_splitter.py auto test_extraction.csv --batch-size 50 --template gemini
```

This creates:
- `batch_001.csv`, `batch_002.csv`, etc. (data files)
- `ai_prompt_batch_001.txt`, `ai_prompt_batch_002.txt`, etc. (ready-to-use prompts)

### Step 2: Copy-Paste Commands for Gemini

Open each `ai_prompt_batch_XXX.txt` file and copy the entire content to Gemini.

## 📋 Exact Prompt Template for Gemini

Copy this prompt and paste your CSV data below it:

```
Translate these Legado e-book app strings from Chinese to English.

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
- Maintain placeholders like %s, %d, \n
- Use consistent terminology

**COMMON TERMS**:
- 阅读 = Reading
- 书源 = Book Sources
- 书架 = Bookshelf  
- 朗读 = Read Aloud
- 设置 = Settings
- 导入 = Import
- 导出 = Export
- 备份 = Backup
- 恢复 = Restore
- 搜索 = Search
- 刷新 = Refresh
- 缓存 = Cache
- 主题 = Theme

CSV Data:
id,type,file_path,line_number,string_name,original_text,translation,context,notes
[PASTE YOUR BATCH DATA HERE]

Please return the complete CSV with all translations filled in the "translation" column.
```

## 🎯 Step-by-Step Workflow

### 1. Create First Batch
```bash
python batch_splitter.py split test_extraction.csv --batch-size 50
```

### 2. Create Gemini Prompt for Batch 1
```bash
python batch_splitter.py prompt batch_001.csv --template gemini
```

### 3. Use Gemini
1. Open `ai_prompt_batch_001.txt`
2. Copy entire content
3. Paste to Gemini AI
4. Wait for response
5. Copy Gemini's CSV response
6. Save as `translated_batch_001.csv`

### 4. Repeat for All Batches
```bash
# For each batch file created:
python batch_splitter.py prompt batch_002.csv --template gemini
python batch_splitter.py prompt batch_003.csv --template gemini
# ... continue for all batches
```

### 5. Merge All Translated Batches
```bash
python batch_splitter.py merge translated_batch_*.csv --output final_translation.csv
```

### 6. Import Back to Project
```bash
python chinese_text_extractor.py import --input final_translation.csv --format csv
```

## 💡 Pro Tips for Gemini

### 1. Optimal Batch Size
- **50 entries** = Best balance of quality and efficiency
- **30 entries** = Higher quality, more requests needed
- **100 entries** = Faster but may reduce quality

### 2. Quality Control Prompts

Add this to your prompt for better consistency:

```
**STYLE REQUIREMENTS**:
- Button text: Keep under 15 characters when possible
- Menu items: Clear and descriptive
- Error messages: Helpful and user-friendly
- Settings: Use standard Android terminology
- Actions: Use active voice (e.g., "Download" not "Downloading")

**TECHNICAL TERMS CONSISTENCY**:
- 书源 = "Book Sources" (always plural)
- 阅读界面 = "Reading Interface" 
- 朗读 = "Read Aloud" (for TTS feature)
- 替换净化 = "Text Replacement"
- 离线缓存 = "Offline Cache"
```

### 3. Example Conversation with Gemini

**You:**
```
Translate these Legado e-book app strings from Chinese to English.

**CONTEXT**: Legado is an Android e-book reader app with book sources, TTS, themes, etc.

CSV Data:
id,type,file_path,line_number,string_name,original_text,translation,context,notes
1,xml_string,app\src\main\res\values-zh\strings.xml,3,app_name,阅读,,String resource: app_name,Chinese parts: 阅读
2,xml_string,app\src\main\res\values-zh\strings.xml,46,bookshelf,书架,,String resource: bookshelf,Chinese parts: 书架

Please return complete CSV with translations.
```

**Gemini should respond:**
```csv
id,type,file_path,line_number,string_name,original_text,translation,context,notes
1,xml_string,app\src\main\res\values-zh\strings.xml,3,app_name,阅读,Reading,String resource: app_name,Chinese parts: 阅读
2,xml_string,app\src\main\res\values-zh\strings.xml,46,bookshelf,书架,Bookshelf,String resource: bookshelf,Chinese parts: 书架
```

## 🔧 Troubleshooting Gemini Responses

### If Gemini Returns Incomplete CSV:
```
Please provide the complete CSV format with all columns intact. I need the exact same structure with only the "translation" column filled in.
```

### If Translations Are Inconsistent:
```
Please ensure consistency with these terms:
- 书源 should always be "Book Sources"
- 设置 should always be "Settings"  
- 阅读 should be "Reading"

Revise the translations to be consistent.
```

### If Format Is Wrong:
```
Please return exactly this CSV format:
id,type,file_path,line_number,string_name,original_text,translation,context,notes

With all the same data but translations added to the "translation" column.
```

## 📊 Expected Results

With 5,838 total entries and batches of 50:
- **117 batches** total
- **About 2-3 hours** of AI translation work
- **High quality** translations due to context and consistency

## 🚀 Quick Commands Summary

```bash
# 1. Auto-create batches and prompts
python batch_splitter.py auto test_extraction.csv --template gemini

# 2. Use Gemini with ai_prompt_batch_*.txt files

# 3. Save Gemini responses as translated_batch_*.csv

# 4. Merge all translations
python batch_splitter.py merge translated_batch_*.csv

# 5. Import to project  
python chinese_text_extractor.py import --input merged_translation.csv --format csv
```

This workflow will give you professional-quality English translations for the entire Legado project! 🎉