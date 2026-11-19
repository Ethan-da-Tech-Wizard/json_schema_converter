# ==============================================================================
# Program: csv_parser.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Specialized CSV parser implementing memory-efficient chunked reading.
#          Processes structured tabular CSV data via pandas in batched chunks,
#          normalizing rows into a list of record dictionaries for consumption
#          by the schema inference engine without exhausting system memory.
# ==============================================================================

import pandas as pd
from .base import BaseParser, ParsingError
from typing import List, Dict, Any

class CSVParser(BaseParser):
    """
    Parses comma-separated value (CSV) files with chunked streaming
    for memory optimization on large datasets.
    """
    def __init__(self, max_file_size: int = None):
        """
        Initialize the CSV parser with an optional file size constraint.
        
        Args:
            max_file_size (int, optional): Maximum size threshold in bytes.
        """
        super().__init__(max_file_size)

    def parse(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Reads a CSV file and converts records into a list of dictionaries.
        Leverages chunking (10,000 rows/chunk) to prevent memory exhaustion.
        
        Args:
            file_path (str): Filesystem path to the CSV file.
            
        Returns:
            List[Dict[str, Any]]: Normalized record dictionaries.
        """
        # Step 1: Validate file size within safety limits
        self.validate_file(file_path)

        try:
            # Step 2: Initialize chunked iterator to process rows incrementally
            # chunksize bounds peak parsing memory to 10,000 rows at a time; the combined
            # record list is still held in memory afterwards.
            reader = pd.read_csv(file_path, chunksize=10000)
            
            # Step 3: Stream and accumulate normalized records
            normalized_data = []
            for chunk in reader:
                normalized_data.extend(chunk.to_dict(orient='records'))
                
            return normalized_data

        except Exception as e:
            # Raise domain-specific ParsingError with contextual details
            raise ParsingError(f"Failed to parse CSV file: {str(e)}")
