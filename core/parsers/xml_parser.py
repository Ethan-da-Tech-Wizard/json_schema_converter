# ==============================================================================
# Program: xml_parser.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Specialized XML parser implementing BaseParser interface.
#          Uses xmltodict to parse hierarchical XML trees into normalized
#          Python dictionaries, disabling external entity resolution to guard
#          against XML External Entity (XXE) vulnerabilities.
# ==============================================================================

import xmltodict
from .base import BaseParser

class XMLParser(BaseParser):
    """
    Parses XML documents into normalized dictionary structures with security
    guardrails against XXE expansion attacks.
    """
    def __init__(self, max_file_size: int = None):
        """
        Initialize the XML parser with an optional file size constraint.
        
        Args:
            max_file_size (int, optional): Maximum size threshold in bytes.
        """
        super().__init__(max_file_size)

    def parse(self, file_path: str):
        """
        Reads an XML file and converts its tree structure into a dictionary.
        
        Args:
            file_path (str): Filesystem path to the XML file.
            
        Returns:
            Dict[str, Any]: Parsed XML dictionary representation.
        """
        # Step 1: Enforce file size security bounds
        self.validate_file(file_path)

        # Step 2: Read raw XML content
        with open(file_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()

        # Step 3: Parse XML into dict while disabling external entities for security
        return xmltodict.parse(xml_content, resolve_entities=False)
