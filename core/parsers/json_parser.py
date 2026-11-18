# Program: json_schema_converter - json_parser.py
# Programmer: Ethan-da-Tech-Wizard (written with Claude, an AI assistant)
# Last Modified: 2026-11-18
# Purpose: Defines JSONParser, which loads a .json file into a Python dict or list after the size check.

"""
JSON Parser Implementation.
Rationale: While JSON is already "structured," we pass it through a parser to ensure 
it is valid before it hits the inference engine. This maintains a consistent 
pipeline where ALL data (CSV, XML, etc.) is treated as a generic Python structure.
"""
# This line imports the standard JSON library to read .json files
import json
# This line imports the BaseParser class we defined earlier so we can follow its rules
from .base import BaseParser

# This line defines the JSONParser class which specializes in reading JSON data
class JSONParser(BaseParser):
    """Parser for .json files."""
    
    # This line allows the JSONParser to accept a custom file size limit
    def __init__(self, max_file_size=None):
        """Pass the optional file size limit up to BaseParser."""
        # This line calls the parent (BaseParser) constructor to set the limit
        super().__init__(max_file_size)

    # This method takes a file path and turns its content into a Python object
    def parse(self, file_path: str):
        """
        Loads a JSON file and returns the native Python representation.
        """
        # This line runs our security check to make sure the file isn't too large
        self.validate_file(file_path)

        # This line opens the file at 'file_path' in 'r' (read) mode
        with open(file_path, 'r') as f:
            # This line reads the text in the file and converts it into a Python dictionary or list
            return json.load(f)
