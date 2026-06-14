"""
Standalone Execution Script (run.py).
Rationale: This provides a zero-boilerplate entry point. It uses a registry-style 
lookup to find the correct parser based on file extension, which is the most 
intuitive UX for a tool like this.
"""
# This line imports sys to handle system-level parameters and paths
import sys
# This line imports os to interact with the operating system (like paths)
import os
# This line imports argparse to handle complex command line options
import argparse
# This line imports Path to handle file paths in a cross-platform way
from pathlib import Path

# This line adds the folder above 'scripts' to Python's search path so we can import the 'core' folder
sys.path.append(str(Path(__file__).parent.parent))

# These lines import the core schema engine and all the specialized parsers we built
from core.engine import SchemaEngine
from core.parsers.json_parser import JSONParser
from core.parsers.csv_parser import CSVParser
from core.parsers.xml_parser import XMLParser
from core.parsers.yaml_parser import YAMLParser
from core.parsers.excel_parser import ExcelParser
# This line imports the SecurityError we defined in the base parser
from core.parsers.base import SecurityError

# This is the main function that runs when you execute the script
def main():
    # This line creates a parser to handle command line arguments
    parser = argparse.ArgumentParser(description="Universal JSON Schema Converter")
    
    # This line adds the required argument: the path to the input file OR directory
    parser.add_argument("input", help="Path to the file or directory you want to convert")
    
    # This line adds an optional argument to override the 1GB safety limit
    # Rationale: Setting this to 0 disables the check entirely (Unlimited Mode)
    parser.add_argument("--max-size", type=int, default=1024, help="Maximum file size in MB (default: 1024, use 0 for unlimited)")
    
    # This line adds the "Strict" toggle to force all fields to be required
    parser.add_argument("--strict", action="store_true", help="Force all fields to be 'required' in the schema")
    
    # This line actually parses the arguments provided by the user in the terminal
    args = parser.parse_args()

    # This line captures the input path from the arguments
    input_path = args.input
    # This line converts the user-provided MB limit into bytes
    max_bytes = args.max_size * 1024 * 1024
    
    # This block checks if the input actually exists
    if not os.path.exists(input_path):
        print(f"Error: Path not found at '{input_path}'")
        sys.exit(1)

    # This line prepares our Schema Engine with the user's "Strict" preference
    engine = SchemaEngine(strict=args.strict)
    
    # This is the "Registry" - it maps file extensions to the correct parser tool
    parsers = {
        '.json': JSONParser(max_file_size=max_bytes),
        '.csv': CSVParser(max_file_size=max_bytes),
        '.xml': XMLParser(max_file_size=max_bytes),
        '.yaml': YAMLParser(max_file_size=max_bytes),
        '.yml': YAMLParser(max_file_size=max_bytes),
        '.xlsx': ExcelParser(max_file_size=max_bytes),
    }

    # This block handles BATCH MERGING if a directory was provided
    if os.path.isdir(input_path):
        print(f"Batch Mode: Searching for files in {input_path}...")
        # This line gets all files in the folder
        files = [os.path.join(input_path, f) for f in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, f))]
        processed_count = 0
        
        # This loop goes through every file found in the folder
        for file in files:
            ext = Path(file).suffix.lower()
            # If we have a parser for this file, we add its data to our "Master Schema"
            if ext in parsers:
                try:
                    # 1. Parse the file
                    data = parsers[ext].parse(file)
                    # 2. Add the data to our engine (this builds the merged schema)
                    engine.add_data(data)
                    processed_count += 1
                except Exception as e:
                    print(f"Warning: Skipping {file} due to error: {e}")
        
        # This block checks if we actually found anything to merge
        if processed_count > 0:
            # This line saves the final Master Schema
            output_path = os.path.join(input_path, "master_schema.json")
            engine.save_schema(engine.get_schema(), output_path)
            print(f"Success! Master Schema created for {processed_count} files at: {output_path}")
        else:
            print("Error: No supported files found in the directory.")
            sys.exit(1)

    # This block handles SINGLE FILE conversion (the original mode)
    else:
        ext = Path(input_path).suffix.lower()
        if ext not in parsers:
            print(f"Error: Unsupported file format '{ext}'")
            sys.exit(1)

        try:
            # 1. Select the correct parser
            active_parser = parsers[ext]
            # 2. Parse the data
            data = active_parser.parse(input_path)
            # 3. Add data to the engine
            engine.add_data(data)
            # 4. Save the schema
            output_path = f"{input_path}.schema.json"
            engine.save_schema(engine.get_schema(), output_path)
            print(f"Success! Schema created at: {output_path}")
        except SecurityError as se:
            print(f"SECURITY ALERT: {se}")
            sys.exit(1)
        except Exception as e:
            print(f"Critical Error: {e}")
            sys.exit(1)

# This line tells Python to run the main() function if this script is executed directly
if __name__ == "__main__":
    main()
