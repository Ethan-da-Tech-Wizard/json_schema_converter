"""
XML Parser Implementation.
Rationale: XML is a tree-based format. To infer a JSON Schema, we must first 
"flatten" it into a Python dictionary. `xmltodict` is the industry standard for 
this, as it handles attributes (prefixed with @) and text nodes (#text) 
in a way that maps cleanly to JSON-like structures.
"""
# This line imports the xmltodict library which makes working with XML as easy as JSON
import xmltodict
# This line imports our BaseParser to ensure we implement the 'parse' method correctly
from .base import BaseParser

# This line defines the XMLParser class for handling XML (Extensible Markup Language)
class XMLParser(BaseParser):
    
    # This line allows the XMLParser to accept a custom file size limit
    def __init__(self, max_file_size=None):
        # This line calls the parent (BaseParser) constructor to set the limit
        super().__init__(max_file_size)

    # This method reads an XML file and converts its tree structure into a dictionary
    def parse(self, file_path: str):
        """
        Reads an XML file and converts it to a dictionary.
        """
        # This line runs our security check to make sure the file isn't too large
        self.validate_file(file_path)

        # This line opens the XML file in 'r' (read) mode
        with open(file_path, 'r') as f:
            # This line reads the entire text content of the file
            xml_content = f.read()
            # This line uses xmltodict with resolve_entities=False to prevent XXE (External Entity) attacks
            # By setting resolve_entities to False, we prevent the parser from reading files on your computer
            return xmltodict.parse(xml_content, resolve_entities=False)
