"""
Base Parser Class for the Universal JSON Schema Converter.
Rationale: Every file format (CSV, XML, etc.) needs to be normalized into a standard Python object 
(dict or list) before GenSON can infer the schema. This base class enforces that contract.
"""
# This line imports the ABC (Abstract Base Class) and abstractmethod decorator from the abc module
from abc import ABC, abstractmethod
# This line imports the os module to check file properties like size
import os
# This line imports List and Any from typing to provide professional type hints
from typing import List, Any, Union, Dict

# This line defines a custom error for security-related failures
class SecurityError(Exception):
    # This line allows the error to carry a message
    pass

# This line defines a custom error for failures that happen during file reading
class ParsingError(Exception):
    # This line allows the error to carry a message
    pass

# This line defines a new class called BaseParser that inherits from ABC (Abstract Base Class)
class BaseParser(ABC):
    
    # This line sets the default safety limit for file sizes to 1GB (1024MB)
    DEFAULT_MAX_SIZE: int = 1024 * 1024 * 1024 # 1 Gigabyte in bytes

    # This method runs when a new parser is created
    def __init__(self, max_file_size: int = None):
        # This line sets the specific limit for this parser instance, or uses the default
        self.max_file_size = max_file_size if max_file_size is not None else self.DEFAULT_MAX_SIZE

    # This method checks if a file is safe to open based on its size
    def validate_file(self, file_path: str) -> None:
        # This block checks if the safety limit is disabled (set to 0)
        if self.max_file_size == 0:
            # This line skips the check entirely and returns early
            return

        # This line gets the size of the file in bytes from the operating system
        file_size = os.path.getsize(file_path)
        # This block checks if the file is larger than our allowed limit
        if file_size > self.max_file_size:
            # This line calculates the size in MB for the error message
            size_mb = self.max_file_size / (1024 * 1024)
            # This line raises a security error if the file is too big
            raise SecurityError(f"File size exceeds {size_mb}MB safety limit. Size: {file_size} bytes")

    # This decorator tells Python that any class using BaseParser MUST implement the 'parse' method
    @abstractmethod
    def parse(self, file_path: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Parses the file and returns a Python dictionary or list.
        """
        # This is a placeholder that does nothing; it will be overridden by real code in sub-classes
        pass
