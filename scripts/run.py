# ==============================================================================
# Program: run.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Standalone CLI entry point for Universal JSON Schema Converter.
#          Dispatches files or directories to appropriate format parsers via
#          an extension registry, supports single-file conversion as well as
#          batch aggregation into a master unified schema, and exposes CLI
#          flags for strict requirement rules and size limits.
# ==============================================================================

import sys
import os
import argparse
from pathlib import Path

# Add project root directory to sys.path to enable core imports
sys.path.append(str(Path(__file__).parent.parent))

from core.engine import SchemaEngine
from core.parsers.json_parser import JSONParser
from core.parsers.csv_parser import CSVParser
from core.parsers.xml_parser import XMLParser
from core.parsers.yaml_parser import YAMLParser
from core.parsers.excel_parser import ExcelParser
from core.parsers.base import SecurityError

def main():
    """
    Main CLI routine for parsing command-line flags and executing schema conversion.
    """
    # Step 1: Initialize argument parser and define CLI interface
    parser = argparse.ArgumentParser(description="Universal JSON Schema Converter")
    parser.add_argument("input", help="Path to the file or directory you want to convert")
    parser.add_argument("--max-size", type=int, default=1024, help="Maximum file size in MB (default: 1024, use 0 for unlimited)")
    parser.add_argument("--strict", action="store_true", help="Force all fields to be 'required' in the schema")
    
    # Step 2: Parse command-line arguments
    args = parser.parse_args()
    input_path = args.input
    max_bytes = args.max_size * 1024 * 1024
    
    # Step 3: Validate input path existence
    if not os.path.exists(input_path):
        print(f"Error: Path not found at '{input_path}'")
        sys.exit(1)

    # Step 4: Instantiate schema engine with configured strictness
    engine = SchemaEngine(strict=args.strict)
    
    # Step 5: Configure parser registry mapped by file extension
    parsers = {
        '.json': JSONParser(max_file_size=max_bytes),
        '.csv': CSVParser(max_file_size=max_bytes),
        '.xml': XMLParser(max_file_size=max_bytes),
        '.yaml': YAMLParser(max_file_size=max_bytes),
        '.yml': YAMLParser(max_file_size=max_bytes),
        '.xlsx': ExcelParser(max_file_size=max_bytes),
    }

    # Step 6: Handle batch directory processing or single-file processing
    if os.path.isdir(input_path):
        print(f"Batch Mode: Searching for files in {input_path}...")
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
        processed_count = 0
        
        # Iterate over directory contents and aggregate schema data
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in parsers:
                try:
                    data = parsers[ext].parse(file)
                    engine.add_data(data)
                    processed_count += 1
                except Exception as e:
                    print(f"Warning: Skipping {file} due to error: {e}")
        
        # Save aggregated master schema if files were processed
        if processed_count > 0:
            output_path = os.path.join(input_path, "master_schema.json")
            engine.save_schema(engine.get_schema(), output_path)
            print(f"Success! Master Schema created for {processed_count} files at: {output_path}")
        else:
            print("Error: No supported files found in the directory.")
            sys.exit(1)

    else:
        # Single-file conversion mode
        ext = Path(input_path).suffix.lower()
        if ext not in parsers:
            print(f"Error: Unsupported file format '{ext}'")
            sys.exit(1)

        try:
            # Parse target file, feed data into engine, and output schema
            active_parser = parsers[ext]
            data = active_parser.parse(input_path)
            engine.add_data(data)
            output_path = f"{input_path}.schema.json"
            engine.save_schema(engine.get_schema(), output_path)
            print(f"Success! Schema created at: {output_path}")
        except SecurityError as se:
            print(f"SECURITY ALERT: {se}")
            sys.exit(1)
        except Exception as e:
            print(f"Critical Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
