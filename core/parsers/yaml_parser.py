"""
YAML Parser Implementation.
Rationale: YAML is a human-friendly superset of JSON. By using `yaml.safe_load`, 
we ensure that we don't execute any arbitrary code embedded in the YAML while 
converting it into a standard Python dictionary for the schema engine.
"""
# This line imports the PyYAML library to handle YAML configuration files
import yaml
# This line imports the BaseParser class to maintain consistency
from .base import BaseParser

# This line defines the YAMLParser class for handling YAML (Yet Another Markup Language)
class YAMLParser(BaseParser):
    
    # This line allows the YAMLParser to accept a custom file size limit
    def __init__(self, max_file_size=None):
        # This line calls the parent (BaseParser) constructor to set the limit
        super().__init__(max_file_size)

    # This method reads a YAML file and converts it into a Python dictionary or list
    def parse(self, file_path: str):
        """
        Reads a YAML file and converts it to a dictionary/list.
        """
        # This line runs our security check to make sure the file isn't too large
        self.validate_file(file_path)

        # This line opens the YAML file in 'r' (read) mode
        with open(file_path, 'r') as f:
            # This line safely loads the YAML content into a Python object (no execution of unsafe code)
            return yaml.safe_load(f)
