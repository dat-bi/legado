# Chinese Text Extraction and Translation Guide for Legado Project

## Overview

This tool helps you extract all Chinese text from the Legado project, translate it externally, and then import the translations back to the correct positions. It handles both XML string resources and hardcoded Chinese text in source code.

## Prerequisites

- Python 3.6 or higher
- Access to the Legado project directory

## Installation

1. Place the `chinese_text_extractor.py` file in your Legado project root directory
2. No additional dependencies required (uses Python standard library only)

## Usage Workflow

### Step 1: Extract Chinese Text

Extract all Chinese text from the project and export to your preferred format:

```bash
# Extract to CSV format (recommended for spreadsheet editing)
python chinese_text_extractor.py extract --format csv --output chinese_texts

# Extract to JSON format (for programmatic processing)
python chinese_text_extractor.py extract --format json --output chinese_texts

# Extract to TXT format (for simple text editing)
python chinese_text_extractor.py extract --format txt --output chinese_texts
```

This will create files like:
- `chinese_texts.csv` - Spreadsheet-friendly format
- `chinese_texts.json` - Structured data format
- `chinese_texts.txt` - Simple text format

### Step 2: Translate the Text

#### Option A: Using CSV (Recommended)
1. Open `chinese_texts.csv` in Excel, Google Sheets, or any spreadsheet software
2. Fill in the `translation` column with your translations
3. Keep the `id`, `type`, `file_path`, and other columns unchanged
4. Save the file

#### Option B: Using JSON
1. Open `chinese_texts.json` in a text editor or JSON editor
2. Fill in the `translation` field for each entry
3. Keep all other fields unchanged
4. Save the file

#### Option C: External Translation Services
You can extract the `original_text` column/field and send it to translation services, then import the results back.

### Step 3: Import Translations

Import your translated text back to the project:

```bash
# Import from CSV
python chinese_text_extractor.py import --input chinese_texts.csv --format csv

# Import from JSON
python chinese_text_extractor.py import --input chinese_texts.json --format json
```

**Important**: The tool automatically creates backups in `backup_before_translation/` directory before making any changes.

### Step 4: Validate Results

Check the translation results and get statistics:

```bash
python chinese_text_extractor.py validate
```

## File Structure

The tool processes these types of files:

### XML String Resources
- `app/src/main/res/values-zh/strings.xml` - Simplified Chinese
- `app/src/main/res/values-zh-rHK/strings.xml` - Hong Kong Traditional Chinese
- `app/src/main/res/values-zh-rTW/strings.xml` - Taiwan Traditional Chinese
- `app/src/main/res/values-zh*/arrays.xml` - Array string resources

### Source Code Files
- `app/src/main/java/**/*.kt` - Kotlin files
- `app/src/main/java/**/*.java` - Java files
- `modules/**/*.kt` - Module Kotlin files
- `modules/**/*.java` - Module Java files

## Output Format Details

### CSV Format
Columns:
- `id` - Unique identifier for each text entry
- `type` - Type of text (xml_string, xml_array_item, source_code)
- `file_path` - Relative path to the file
- `line_number` - Line number in the file
- `string_name` - Name of the string resource (for XML)
- `original_text` - Original Chinese text
- `translation` - Your translation (fill this in)
- `context` - Context information
- `notes` - Additional notes

### JSON Format
```json
{
  "metadata": {
    "project": "Legado",
    "extracted_at": "2024-01-01T12:00:00",
    "total_entries": 1000
  },
  "entries": [
    {
      "id": 1,
      "type": "xml_string",
      "file_path": "app/src/main/res/values-zh/strings.xml",
      "line_number": 45,
      "string_name": "app_name",
      "original_text": "阅读",
      "translation": "",
      "context": "String resource: app_name",
      "chinese_parts": ["阅读"]
    }
  ]
}
```

## Safety Features

1. **Automatic Backup**: Creates backup copies before any modifications
2. **Non-destructive**: Only modifies files if translations are provided
3. **Validation**: Checks file integrity and provides statistics
4. **Reversible**: You can restore from backups if needed

## Best Practices

1. **Always backup**: Though the tool creates backups, make your own backup of important files
2. **Test translations**: After importing, test the app to ensure proper display
3. **Validate thoroughly**: Use the validate command to check completeness
4. **Incremental translation**: You can translate and import in batches
5. **Review context**: Pay attention to the context field for better translations

## Troubleshooting

### Common Issues

1. **Encoding errors**: Make sure your translated files are saved in UTF-8 encoding
2. **Missing translations**: Empty translation fields are skipped during import
3. **File permissions**: Ensure you have write permissions to the project files
4. **XML malformed**: If XML files become malformed, restore from backup

### Recovery

If something goes wrong:
1. Check the `backup_before_translation/` directory
2. Copy files back from backup to restore original state
3. Re-run the extraction and fix any issues in your translation file

## Advanced Usage

### Filtering Specific Files
You can modify the patterns in the script to focus on specific files or directories.

### Custom Translation Pipeline
The JSON format is ideal for integrating with translation APIs or custom processing pipelines.

### Batch Processing
You can process multiple language variants by running the tool separately for each target language.

## Support and Contributions

This tool is designed for the Legado project's translation workflow. If you encounter issues or have suggestions for improvements, please document them for future versions.

## Example Workflow

```bash
# 1. Extract all Chinese text
python chinese_text_extractor.py extract --format csv --output my_translation

# 2. Edit my_translation.csv in Excel/Google Sheets
# Fill in the translation column

# 3. Import translations back to project
python chinese_text_extractor.py import --input my_translation.csv --format csv

# 4. Validate the results
python chinese_text_extractor.py validate

# 5. Test your app to ensure everything works correctly
```

This workflow allows you to efficiently manage large-scale translation projects while maintaining the integrity of the original codebase.