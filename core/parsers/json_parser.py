# ==============================================================================
# Program: json_parser.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Specialized JSON parser implementing BaseParser interface.
#          Validates file boundaries and parses valid JSON into native Python
#          dictionaries or lists for the schema inference engine pipeline.
# ==============================================================================

import json
from .base import BaseParser

class JSONParser(BaseParser):
    """
    Parses JSON data files into native Python objects while enforcing
    security bounds.
    """
    def __init__(self, max_file_size: int = None):
        """
        Initialize the JSON parser with an optional file size constraint.
        
        Args:
            max_file_size (int, optional): Maximum size threshold in bytes.
        """
        super().__init__(max_file_size)

    def parse(self, file_path: str):
        """
        Loads and parses a JSON file into native Python representations.
        
        Args:
            file_path (str): Filesystem path to target JSON file.
            
        Returns:
            Union[Dict, List]: Deserialized JSON structure.
        """
        # Step 1: Enforce file size security bounds
        self.validate_file(file_path)

        # Step 2: Open target file and deserialize JSON content
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
