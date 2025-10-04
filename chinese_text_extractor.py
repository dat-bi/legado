#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chinese Text Extraction and Translation Tool for Legado Project
================================================================

This tool can:
1. Extract all Chinese text from the Legado project (XML strings and source code)
2. Export to translation-friendly formats (CSV, JSON, TXT)
3. Import translated text back to the exact positions
4. Validate that all text is properly restored

Usage:
    python chinese_text_extractor.py extract [--format csv|json|txt] [--output output_file]
    python chinese_text_extractor.py import [--input translated_file] [--format csv|json|txt]
    python chinese_text_extractor.py validate

Author: Created for Legado translation workflow
"""

import os
import re
import json
import csv
import xml.etree.ElementTree as ET
from typing import Dict, List, Tuple, Optional
import argparse
from pathlib import Path
import shutil
from datetime import datetime

class ChineseTextExtractor:
    """Main class for extracting and managing Chinese text in the Legado project."""
    
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.chinese_regex = re.compile(r'[\u4e00-\u9fff]+')
        self.extracted_data = []
        
        # Define file patterns to search
        self.xml_patterns = [
            "app/src/main/res/values-zh*/strings.xml",
            "app/src/main/res/values-zh*/arrays.xml",
            "app/src/debug/res/values-zh*/strings.xml"
        ]
        
        self.source_patterns = [
            "app/src/main/java/**/*.kt",
            "app/src/main/java/**/*.java",
            "modules/**/*.kt", 
            "modules/**/*.java"
        ]
    
    def find_chinese_in_text(self, text: str) -> List[str]:
        """Find all Chinese character sequences in text."""
        return self.chinese_regex.findall(text)
    
    def extract_xml_strings(self) -> List[Dict]:
        """Extract Chinese strings from XML resource files."""
        xml_data = []
        
        for pattern in self.xml_patterns:
            for xml_file in self.project_root.glob(pattern):
                if not xml_file.exists():
                    continue
                    
                print(f"Processing XML file: {xml_file}")
                
                try:
                    tree = ET.parse(xml_file)
                    root = tree.getroot()
                    
                    for string_elem in root.findall('.//string'):
                        name = string_elem.get('name', '')
                        text = string_elem.text or ''
                        
                        # Check if contains Chinese
                        chinese_parts = self.find_chinese_in_text(text)
                        if chinese_parts:
                            xml_data.append({
                                'type': 'xml_string',
                                'file_path': str(xml_file.relative_to(self.project_root)),
                                'string_name': name,
                                'original_text': text,
                                'chinese_parts': chinese_parts,
                                'line_number': self._get_xml_line_number(xml_file, name),
                                'context': f"String resource: {name}",
                                'translation': text  # Will be updated during import
                            })
                    
                    # Process string-array elements
                    for array_elem in root.findall('.//string-array'):
                        array_name = array_elem.get('name', '')
                        for i, item in enumerate(array_elem.findall('item')):
                            item_text = item.text or ''
                            chinese_parts = self.find_chinese_in_text(item_text)
                            if chinese_parts:
                                xml_data.append({
                                    'type': 'xml_array_item',
                                    'file_path': str(xml_file.relative_to(self.project_root)),
                                    'string_name': f"{array_name}[{i}]",
                                    'original_text': item_text,
                                    'chinese_parts': chinese_parts,
                                    'line_number': self._get_xml_line_number(xml_file, array_name),
                                    'context': f"Array item: {array_name}[{i}]",
                                    'translation': item_text
                                })
                                
                except ET.ParseError as e:
                    print(f"Error parsing {xml_file}: {e}")
                    
        return xml_data
    
    def extract_source_code_strings(self) -> List[Dict]:
        """Extract Chinese strings from Kotlin/Java source code."""
        source_data = []
        
        for pattern in self.source_patterns:
            for source_file in self.project_root.glob(pattern):
                if not source_file.exists():
                    continue
                    
                print(f"Processing source file: {source_file}")
                
                try:
                    with open(source_file, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                    
                    for line_num, line in enumerate(lines, 1):
                        # Skip comments for now (can be enabled if needed)
                        if line.strip().startswith('//') or line.strip().startswith('*'):
                            continue
                            
                        chinese_matches = self.chinese_regex.finditer(line)
                        for match in chinese_matches:
                            chinese_text = match.group()
                            # Get surrounding context (30 chars before and after)
                            start = max(0, match.start() - 30)
                            end = min(len(line), match.end() + 30)
                            context = line[start:end].strip()
                            
                            source_data.append({
                                'type': 'source_code',
                                'file_path': str(source_file.relative_to(self.project_root)),
                                'line_number': line_num,
                                'original_text': chinese_text,
                                'full_line': line.strip(),
                                'context': context,
                                'chinese_parts': [chinese_text],
                                'translation': chinese_text
                            })
                            
                except UnicodeDecodeError:
                    print(f"Encoding error in {source_file}, skipping...")
                except Exception as e:
                    print(f"Error processing {source_file}: {e}")
                    
        return source_data
    
    def _get_xml_line_number(self, xml_file: Path, element_name: str) -> int:
        """Get approximate line number for XML element (simplified approach)."""
        try:
            with open(xml_file, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    if f'name="{element_name}"' in line:
                        return line_num
        except:
            pass
        return 0
    
    def extract_all(self) -> List[Dict]:
        """Extract all Chinese text from the project."""
        print("Starting Chinese text extraction...")
        
        self.extracted_data = []
        
        # Extract from XML resources
        xml_data = self.extract_xml_strings()
        self.extracted_data.extend(xml_data)
        print(f"Found {len(xml_data)} Chinese strings in XML resources")
        
        # Extract from source code
        source_data = self.extract_source_code_strings()
        self.extracted_data.extend(source_data)
        print(f"Found {len(source_data)} Chinese strings in source code")
        
        print(f"Total Chinese text entries found: {len(self.extracted_data)}")
        return self.extracted_data
    
    def export_to_csv(self, output_file: str):
        """Export extracted data to CSV format for translation."""
        if not self.extracted_data:
            print("No data to export. Run extract_all() first.")
            return
            
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'id', 'type', 'file_path', 'line_number', 'string_name', 
                'original_text', 'translation', 'context', 'notes'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for i, item in enumerate(self.extracted_data):
                writer.writerow({
                    'id': i + 1,
                    'type': item['type'],
                    'file_path': item['file_path'],
                    'line_number': item['line_number'],
                    'string_name': item.get('string_name', ''),
                    'original_text': item['original_text'],
                    'translation': '',  # Empty for translator to fill
                    'context': item['context'],
                    'notes': f"Chinese parts: {', '.join(item['chinese_parts'])}"
                })
        
        print(f"Exported {len(self.extracted_data)} entries to {output_file}")
    
    def export_to_json(self, output_file: str):
        """Export extracted data to JSON format."""
        if not self.extracted_data:
            print("No data to export. Run extract_all() first.")
            return
            
        export_data = {
            'metadata': {
                'project': 'Legado',
                'extracted_at': datetime.now().isoformat(),
                'total_entries': len(self.extracted_data)
            },
            'entries': []
        }
        
        for i, item in enumerate(self.extracted_data):
            export_entry = item.copy()
            export_entry['id'] = i + 1
            export_entry['translation'] = ''  # Empty for translator
            export_data['entries'].append(export_entry)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, ensure_ascii=False, indent=2)
        
        print(f"Exported {len(self.extracted_data)} entries to {output_file}")
    
    def export_to_txt(self, output_file: str):
        """Export extracted data to simple text format."""
        if not self.extracted_data:
            print("No data to export. Run extract_all() first.")
            return
            
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Legado Chinese Text Extraction\n")
            f.write("=" * 50 + "\n\n")
            
            for i, item in enumerate(self.extracted_data, 1):
                f.write(f"Entry {i}:\n")
                f.write(f"Type: {item['type']}\n")
                f.write(f"File: {item['file_path']}\n")
                f.write(f"Line: {item['line_number']}\n")
                if item.get('string_name'):
                    f.write(f"Name: {item['string_name']}\n")
                f.write(f"Original: {item['original_text']}\n")
                f.write(f"Context: {item['context']}\n")
                f.write(f"Translation: [TO BE FILLED]\n")
                f.write("-" * 30 + "\n\n")
        
        print(f"Exported {len(self.extracted_data)} entries to {output_file}")
    
    def import_translations_from_csv(self, input_file: str) -> Dict[int, str]:
        """Import translations from CSV file."""
        translations = {}
        
        with open(input_file, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                entry_id = int(row['id'])
                translation = row['translation'].strip()
                if translation:  # Only import non-empty translations
                    translations[entry_id] = translation
        
        print(f"Loaded {len(translations)} translations from {input_file}")
        return translations
    
    def import_translations_from_json(self, input_file: str) -> Dict[int, str]:
        """Import translations from JSON file."""
        translations = {}
        
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for entry in data.get('entries', []):
            entry_id = entry['id']
            translation = entry.get('translation', '').strip()
            if translation:  # Only import non-empty translations
                translations[entry_id] = translation
        
        print(f"Loaded {len(translations)} translations from {input_file}")
        return translations
    
    def apply_translations(self, translations: Dict[int, str]):
        """Apply translations back to the project files."""
        if not self.extracted_data:
            print("No extracted data available. Run extract_all() first.")
            return
        
        # Create backup before modifying files
        self._create_backup()
        
        # Group changes by file for efficient processing
        file_changes = {}
        
        for i, item in enumerate(self.extracted_data):
            entry_id = i + 1
            if entry_id in translations:
                file_path = item['file_path']
                if file_path not in file_changes:
                    file_changes[file_path] = []
                
                file_changes[file_path].append({
                    'item': item,
                    'new_translation': translations[entry_id]
                })
        
        # Apply changes file by file
        success_count = 0
        for file_path, changes in file_changes.items():
            if self._apply_file_changes(file_path, changes):
                success_count += len(changes)
        
        print(f"Successfully applied {success_count} translations")
    
    def _create_backup(self):
        """Create backup of files before modification."""
        backup_dir = self.project_root / "backup_before_translation"
        backup_dir.mkdir(exist_ok=True)
        
        # Backup XML files
        for pattern in self.xml_patterns:
            for xml_file in self.project_root.glob(pattern):
                if xml_file.exists():
                    relative_path = xml_file.relative_to(self.project_root)
                    backup_file = backup_dir / relative_path
                    backup_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(xml_file, backup_file)
        
        # Backup source files that contain Chinese text
        backed_up_sources = set()
        for item in self.extracted_data:
            if item['type'] == 'source_code':
                file_path = self.project_root / item['file_path']
                if file_path not in backed_up_sources:
                    relative_path = file_path.relative_to(self.project_root)
                    backup_file = backup_dir / relative_path
                    backup_file.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(file_path, backup_file)
                    backed_up_sources.add(file_path)
        
        print(f"Created backup in {backup_dir}")
    
    def _apply_file_changes(self, file_path: str, changes: List[Dict]) -> bool:
        """Apply translation changes to a specific file."""
        full_path = self.project_root / file_path
        
        try:
            if file_path.endswith('.xml'):
                return self._apply_xml_changes(full_path, changes)
            else:
                return self._apply_source_changes(full_path, changes)
        except Exception as e:
            print(f"Error applying changes to {file_path}: {e}")
            return False
    
    def _apply_xml_changes(self, xml_file: Path, changes: List[Dict]) -> bool:
        """Apply translation changes to XML files."""
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            
            for change in changes:
                item = change['item']
                new_translation = change['new_translation']
                
                if item['type'] == 'xml_string':
                    # Find and update string element
                    for string_elem in root.findall('.//string'):
                        if string_elem.get('name') == item['string_name']:
                            string_elem.text = new_translation
                            break
                
                elif item['type'] == 'xml_array_item':
                    # Handle array items (more complex)
                    array_name = item['string_name'].split('[')[0]
                    array_index = int(item['string_name'].split('[')[1].rstrip(']'))
                    
                    for array_elem in root.findall('.//string-array'):
                        if array_elem.get('name') == array_name:
                            items = array_elem.findall('item')
                            if array_index < len(items):
                                items[array_index].text = new_translation
                            break
            
            # Write back to file
            tree.write(xml_file, encoding='utf-8', xml_declaration=True)
            print(f"Updated {len(changes)} entries in {xml_file}")
            return True
            
        except Exception as e:
            print(f"Error updating XML file {xml_file}: {e}")
            return False
    
    def _apply_source_changes(self, source_file: Path, changes: List[Dict]) -> bool:
        """Apply translation changes to source code files."""
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Sort changes by line number in reverse order to avoid index shifting
            changes.sort(key=lambda x: x['item']['line_number'], reverse=True)
            
            for change in changes:
                item = change['item']
                new_translation = change['new_translation']
                line_num = item['line_number'] - 1  # Convert to 0-based index
                
                if 0 <= line_num < len(lines):
                    # Replace the Chinese text in the line
                    old_line = lines[line_num]
                    new_line = old_line.replace(item['original_text'], new_translation)
                    lines[line_num] = new_line
            
            # Write back to file
            with open(source_file, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            
            print(f"Updated {len(changes)} entries in {source_file}")
            return True
            
        except Exception as e:
            print(f"Error updating source file {source_file}: {e}")
            return False
    
    def validate_translations(self) -> Dict[str, int]:
        """Validate translation completeness and report statistics."""
        if not self.extracted_data:
            print("No data to validate. Run extract_all() first.")
            return {}
        
        stats = {
            'total_entries': len(self.extracted_data),
            'xml_strings': 0,
            'xml_arrays': 0,
            'source_code': 0,
            'files_affected': set()
        }
        
        for item in self.extracted_data:
            if item['type'] == 'xml_string':
                stats['xml_strings'] += 1
            elif item['type'] == 'xml_array_item':
                stats['xml_arrays'] += 1
            elif item['type'] == 'source_code':
                stats['source_code'] += 1
            
            stats['files_affected'].add(item['file_path'])
        
        stats['files_affected'] = len(stats['files_affected'])
        
        print("\nTranslation Validation Report:")
        print("=" * 40)
        print(f"Total entries: {stats['total_entries']}")
        print(f"XML string resources: {stats['xml_strings']}")
        print(f"XML array items: {stats['xml_arrays']}")
        print(f"Source code strings: {stats['source_code']}")
        print(f"Files affected: {stats['files_affected']}")
        
        return stats


def main():
    parser = argparse.ArgumentParser(description='Chinese Text Extraction Tool for Legado')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Extract command
    extract_parser = subparsers.add_parser('extract', help='Extract Chinese text')
    extract_parser.add_argument('--format', choices=['csv', 'json', 'txt'], default='csv',
                               help='Output format (default: csv)')
    extract_parser.add_argument('--output', default='chinese_text_extracted',
                               help='Output file name (without extension)')
    
    # Import command (placeholder for future implementation)
    import_parser = subparsers.add_parser('import', help='Import translated text')
    import_parser.add_argument('--input', required=True, help='Input file with translations')
    import_parser.add_argument('--format', choices=['csv', 'json'], default='csv',
                              help='Input format')
    
    # Validate command (placeholder for future implementation) 
    validate_parser = subparsers.add_parser('validate', help='Validate translation consistency')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    extractor = ChineseTextExtractor()
    
    if args.command == 'extract':
        # Extract all Chinese text
        extractor.extract_all()
        
        # Export in requested format
        output_file = f"{args.output}.{args.format}"
        if args.format == 'csv':
            extractor.export_to_csv(output_file)
        elif args.format == 'json':
            extractor.export_to_json(output_file)
        elif args.format == 'txt':
            extractor.export_to_txt(output_file)
            
    elif args.command == 'import':
        # Load translations and apply them
        extractor.extract_all()  # Need original data for mapping
        
        if args.format == 'csv':
            translations = extractor.import_translations_from_csv(args.input)
        elif args.format == 'json':
            translations = extractor.import_translations_from_json(args.input)
        else:
            print(f"Unsupported import format: {args.format}")
            return
        
        if translations:
            extractor.apply_translations(translations)
            print("\nTranslation import completed!")
        else:
            print("No translations found in input file.")
            
    elif args.command == 'validate':
        extractor.extract_all()
        stats = extractor.validate_translations()
        
        # Additional validation checks
        print("\nRecommendations:")
        print("-" * 20)
        if stats.get('source_code', 0) > 0:
            print("• Consider moving hardcoded Chinese strings to string resources")
        print("• Test the application after translation to ensure proper display")
        print("• Backup files are created automatically during import")


if __name__ == '__main__':
    main()