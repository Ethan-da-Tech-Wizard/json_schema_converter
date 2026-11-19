# ==============================================================================
# Program: yaml_parser.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Specialized YAML parser implementing BaseParser interface.
#          Uses yaml.safe_load to parse YAML document trees into native Python
#          dictionaries or lists without executing untrusted arbitrary code.
# ==============================================================================

import yaml
from .base import BaseParser

class YAMLParser(BaseParser):
    """
    Parses YAML documents into native Python data structures using safe loading.
    """
    def __init__(self, max_file_size: int = None):
        """
        Initialize the YAML parser with an optional file size constraint.
        
        Args:
            max_file_size (int, optional): Maximum size threshold in bytes.
        """
        super().__init__(max_file_size)

    def parse(self, file_path: str):
        """
        Reads a YAML file and safely deserializes its content.
        
        Args:
            file_path (str): Filesystem path to the YAML file.
            
        Returns:
            Union[Dict, List]: Deserialized YAML data.
        """
        # Step 1: Enforce file size security bounds
        self.validate_file(file_path)

        # Step 2: Open and safely parse YAML content
        # safe_load builds only plain Python types; unlike yaml.load it cannot
        # instantiate arbitrary objects from tags in untrusted files.
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
