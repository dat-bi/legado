# AI Translation Prompts for Legado Chinese Text

## 🤖 Using AI Models (Gemini, ChatGPT, Claude) for Translation

This guide provides optimized prompts and commands to get accurate translations from AI models for the Legado project's Chinese text.

## 📋 Preparation Steps

1. **Extract a manageable batch** (50-100 entries at a time for best results):
```bash
# Extract first 100 entries to a separate file
head -101 test_extraction.csv > batch_001.csv
```

2. **Prepare the context information** about Legado project

## 🎯 Optimized AI Translation Prompts

### For Gemini/ChatGPT/Claude:

```
I need you to translate Chinese text for an Android reading app called "Legado". This is a professional e-book reader app with features like book sources, reading interface, TTS, etc.

**CONTEXT**: Legado is an open-source Android e-book reading application that supports:
- Multiple book sources and formats
- Customizable reading interface
- Text-to-speech functionality  
- Book management and library features
- Web services and import/export

**TRANSLATION REQUIREMENTS**:
1. Translate to natural, user-friendly English
2. Keep technical terms consistent (e.g., "书源" = "Book Sources")
3. Maintain Android UI conventions
4. Consider the context provided for each string
5. Keep formatting placeholders like %s, %d unchanged

**INPUT FORMAT**: CSV with columns: id, type, file_path, line_number, string_name, original_text, translation, context, notes

**YOUR TASK**: Fill in the "translation" column with accurate English translations.

Here's the data to translate:

[PASTE YOUR CSV DATA HERE]

**OUTPUT**: Return the complete CSV with translations filled in the "translation" column.
```

### 🔥 Specific Prompt for Batches:

```
Translate this batch of Legado app strings from Chinese to English:

**PROJECT**: Legado - Open source Android e-book reader
**TASK**: Translate Chinese UI strings to English
**REQUIREMENTS**: 
- Natural English for mobile app users
- Consistent terminology
- Keep %s, %d, \n unchanged
- Consider Android Material Design guidelines

**COMMON TERMS REFERENCE**:
- 阅读 = Reading
- 书源 = Book Sources  
- 书架 = Bookshelf
- 朗读 = Text-to-Speech/Read Aloud
- 搜索 = Search
- 设置 = Settings
- 导入 = Import
- 导出 = Export
- 备份 = Backup
- 恢复 = Restore

CSV Data:
```

### 📱 Context-Aware Prompt:

```
You are translating UI strings for "Legado", a popular Android e-book reader app. 

**APP FEATURES CONTEXT**:
- Book library management
- Multiple book source support
- Customizable reading themes
- TTS (Text-to-Speech) 
- Web-based book editing
- Import/Export functionality
- Chinese/Traditional Chinese support

**TRANSLATION STYLE**:
- Mobile app UI language (concise, clear)
- Follow Android Material Design terminology
- User-friendly, not technical jargon
- Consistent with Google Play Store apps

**SPECIAL INSTRUCTIONS**:
- "阅读" in app name context = "Reading" 
- "书源" = "Book Sources" (not "Book Origin")
- "朗读" = "Read Aloud" or "TTS" depending on context
- Keep button text short (under 15 characters when possible)
- Menu items should be descriptive but concise

Please translate this CSV data:
```

## 🛠️ Automated Batch Processing Commands

### 1. Split large CSV into smaller batches:

```bash
# Create batches of 50 entries each (Windows)
python -c "
import csv
import math

# Read the main extraction file
with open('test_extraction.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    rows = list(reader)

header = rows[0]
data_rows = rows[1:]
batch_size = 50
num_batches = math.ceil(len(data_rows) / batch_size)

for i in range(num_batches):
    start_idx = i * batch_size
    end_idx = min((i + 1) * batch_size, len(data_rows))
    batch_rows = data_rows[start_idx:end_idx]
    
    filename = f'batch_{i+1:03d}.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(batch_rows)
    
    print(f'Created {filename} with {len(batch_rows)} entries')
"
```

### 2. Prepare prompt with batch data:

```bash
# Create a prompt file for AI translation
python -c "
import csv

prompt = '''
Translate this Legado app batch from Chinese to English:

**PROJECT**: Legado Android E-book Reader
**CONTEXT**: Open-source reading app with book sources, TTS, themes
**OUTPUT**: Same CSV format with translations in the translation column

CSV Data:
'''

# Read batch file
with open('batch_001.csv', 'r', encoding='utf-8') as f:
    content = f.read()

with open('ai_prompt_batch_001.txt', 'w', encoding='utf-8') as f:
    f.write(prompt + content)

print('Created ai_prompt_batch_001.txt - Copy this to your AI model')
"
```

## 🎨 Example Translations for Reference

```csv
id,original_text,good_translation,context
1,阅读,Reading,App name
2,书架,Bookshelf,Main tab
3,搜索,Search,Action button  
4,设置,Settings,Menu item
5,朗读,Read Aloud,TTS feature
6,书源管理,Book Sources,Menu item
7,主题设置,Theme Settings,Settings category
8,备份与恢复,Backup & Restore,Settings section
9,离线缓存,Offline Cache,Download feature
10,替换净化,Text Replacement,Content filtering
```

## 🔄 Workflow for AI Translation

### Step 1: Prepare Batch
```bash
# Create batch of 50 entries
head -51 test_extraction.csv > batch_001.csv
```

### Step 2: Create AI Prompt
Copy the optimized prompt above and paste your CSV data.

### Step 3: Get Translation from AI
Use Gemini, ChatGPT, or Claude with the prepared prompt.

### Step 4: Save and Import
```bash
# Save AI response as translated_batch_001.csv
# Then import back to project
python chinese_text_extractor.py import --input translated_batch_001.csv --format csv
```

### Step 5: Repeat for Next Batch
```bash
# Get next 50 entries
sed -n '52,102p' test_extraction.csv > temp.csv
echo "$(head -1 test_extraction.csv)" > batch_002.csv
cat temp.csv >> batch_002.csv
```

## 🎯 Quality Tips for AI Translation

1. **Provide Context**: Always mention it's for Android app UI
2. **Use Batches**: 50-100 entries per request for best quality
3. **Be Specific**: Mention Legado's features (e-book, TTS, etc.)
4. **Review Common Terms**: Ensure consistency across batches
5. **Check Format**: Verify CSV structure is maintained
6. **Test Import**: Always test a small batch first

## 🚀 Quick Commands for Different AI Models

### For Gemini:
```
Translate these Legado e-book app strings from Chinese to English. Keep CSV format, fill translation column:

[PASTE CSV DATA]
```

### For ChatGPT:
```
I need English translations for Chinese UI strings from Legado Android app. Maintain CSV format and provide natural, user-friendly translations:

[PASTE CSV DATA]
```

### For Claude:
```
Please translate these Chinese strings for the Legado e-book reader Android app. Return the CSV with English translations in the translation column:

[PASTE CSV DATA]
```

## ⚡ Pro Tips

1. **Start with small batches** (20-30 entries) to test quality
2. **Save successful prompts** that work well for your AI model
3. **Create a terminology glossary** from good translations
4. **Use the context column** to guide translation decisions
5. **Double-check technical terms** and button labels

This approach will give you high-quality, consistent translations for the entire Legado project! 🎉