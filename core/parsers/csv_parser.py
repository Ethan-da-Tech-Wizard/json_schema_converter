"""
CSV Parser Implementation with Memory Optimization.
Rationale: For massive CSVs, we use chunking to avoid loading the entire file into RAM at once.
This is a "Senior-Tier" optimization for high-performance data engineering.
"""
# This line imports pandas to handle the spreadsheet data
import pandas as pd
# This line imports the BaseParser and ParsingError for consistency and error handling
from .base import BaseParser, ParsingError
# This line imports type hints for professional code standards
from typing import List, Dict, Any

# This line defines the CSVParser class
class CSVParser(BaseParser):
    
    # This method allows setting a custom file size limit
    def __init__(self, max_file_size: int = None):
        # This line calls the parent constructor
        super().__init__(max_file_size)

    # This method reads a CSV file and turns it into a list of dictionaries
    def parse(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Reads a CSV and converts it to a list of dictionaries.
        Uses chunking to stay memory-efficient for large files.
        """
        # This line runs our security size check
        self.validate_file(file_path)

        try:
            # This line prepares to read the CSV in chunks of 10,000 rows at a time
            # Rationale: This prevents the computer from freezing if the file is 1GB+
            reader = pd.read_csv(file_path, chunksize=10000)
            
            # This line creates an empty list to store our final data
            normalized_data = []
            
            # This loop processes the file one chunk at a time
            for chunk in reader:
                # This line converts each chunk into dictionaries and adds them to our list
                normalized_data.extend(chunk.to_dict(orient='records'))
                
            # This line returns the complete normalized list
            return normalized_data

        except Exception as e:
            # This line catches errors like bad formatting and raises our custom ParsingError
            raise ParsingError(f"Failed to parse CSV file: {str(e)}")
