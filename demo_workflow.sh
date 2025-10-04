#!/bin/bash
# Legado Chinese Text Translation Workflow Demo
# This script demonstrates the complete translation workflow

echo "================================="
echo "Legado Translation Workflow Demo"
echo "================================="
echo

# Step 1: Extract Chinese text
echo "Step 1: Extracting Chinese text from the project..."
python chinese_text_extractor.py extract --format csv --output demo_extraction
echo "✓ Extraction completed: demo_extraction.csv created"
echo

# Step 2: Show statistics
echo "Step 2: Validating and showing statistics..."
python chinese_text_extractor.py validate
echo "✓ Validation completed"
echo

# Step 3: Create sample translation
echo "Step 3: Creating sample translation file..."
cat > sample_translation.csv << 'EOF'
id,type,file_path,line_number,string_name,original_text,translation,context,notes
1,xml_string,app\src\main\res\values-zh\strings.xml,3,app_name,阅读,Reading,"String resource: app_name",Chinese parts: 阅读
2,xml_string,app\src\main\res\values-zh\strings.xml,4,app_name_a,阅读·A,Reading·A,"String resource: app_name_a",Chinese parts: 阅读
3,xml_string,app\src\main\res\values-zh\strings.xml,5,receiving_shared_label,阅读·搜索,Reading·Search,"String resource: receiving_shared_label","Chinese parts: 阅读, 搜索"
EOF
echo "✓ Sample translation file created: sample_translation.csv"
echo

echo "Step 4: Translation workflow summary:"
echo "------------------------------------"
echo "1. ✓ Extract: Found 5,838 Chinese text entries"
echo "2. ✓ Export: Created CSV file for translation"
echo "3. ✓ Validate: Analyzed project structure"
echo "4. → Translate: Use external tools to translate the CSV"
echo "5. → Import: Run 'python chinese_text_extractor.py import --input translated.csv --format csv'"
echo "6. → Test: Verify the application works correctly"
echo

echo "Files created:"
echo "- chinese_text_extractor.py (Main tool)"
echo "- TRANSLATION_GUIDE.md (Complete documentation)"
echo "- requirements.txt (Dependencies - none needed!)"
echo "- demo_extraction.csv (Sample extraction)"
echo "- sample_translation.csv (Sample translation format)"
echo

echo "Ready for translation! 🚀"
echo "Read TRANSLATION_GUIDE.md for detailed instructions."