# ==============================================================================
# Program: base.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Base abstract parser interface for Universal JSON Schema Converter.
#          Defines standard contracts, file size validation guardrails, and
#          common security checks across all specialized format parsers (CSV,
#          Excel, XML, YAML, JSON). Normalizes input files into generic Python
#          dictionaries or lists for the schema inference engine.
# ==============================================================================

from abc import ABC, abstractmethod
import os
from typing import List, Any, Union, Dict

# Raised before parsing when a file is too big, so oversized input is refused
# instead of being loaded into memory.
class SecurityError(Exception):
    """Custom exception raised when security or file size limits are violated."""
    pass

# Wraps library-specific parse failures (pandas etc.) in one domain error.
class ParsingError(Exception):
    """Custom exception raised when file parsing operations fail."""
    pass

class BaseParser(ABC):
    """
    Abstract base class providing standard validation and contract enforcement
    for file format parsers in the schema conversion pipeline.
    """
    # Default safety limit for file processing: 1 Gigabyte in bytes
    DEFAULT_MAX_SIZE: int = 1024 * 1024 * 1024

    def __init__(self, max_file_size: int = None):
        """
        Initialize the parser with an optional custom maximum file size threshold.
        
        Args:
            max_file_size (int, optional): Maximum allowed size in bytes (0 for unlimited).
        """
        # Assign configured threshold or default to 1GB
        # None means "use the default"; 0 is a deliberate "no limit" and is therefore
        # not treated as falsy here.
        self.max_file_size = max_file_size if max_file_size is not None else self.DEFAULT_MAX_SIZE

    def validate_file(self, file_path: str) -> None:
        """
        Validates target file against size constraints to protect system resources.
        
        Args:
            file_path (str): Filesystem path to the input target.
            
        Raises:
            SecurityError: If file exceeds maximum size threshold.
        """
        # Step 1: If safety limit is explicitly disabled (0), bypass check
        # 0 disables the check entirely (CLI: --max-size 0).
        if self.max_file_size == 0:
            return

        # Step 2: Query filesystem for target file size
        file_size = os.path.getsize(file_path)

        # Step 3: Compare size against enforced maximum threshold
        if file_size > self.max_file_size:
            size_mb = self.max_file_size / (1024 * 1024)
            raise SecurityError(f"File size exceeds {size_mb}MB safety limit. Size: {file_size} bytes")

    # Subclasses return a dict (document formats) or list of dicts (tabular
    # formats); SchemaEngine.add_data accepts either shape.
    @abstractmethod
    def parse(self, file_path: str) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Parse file into a normalized Python dictionary or list of dictionaries.
        Must be implemented by concrete parser subclasses.
        
        Args:
            file_path (str): Path to the source file to parse.
            
        Returns:
            Union[Dict[str, Any], List[Dict[str, Any]]]: Normalized Python data structure.
        """
        pass
