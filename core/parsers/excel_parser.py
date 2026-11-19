# ==============================================================================
# Program: excel_parser.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Specialized Excel (.xlsx) parser implementing BaseParser interface.
#          Uses pandas and openpyxl engine to read spreadsheet sheets and
#          convert tabular records into uniform record dictionaries for
#          schema inference.
# ==============================================================================

import pandas as pd
from .base import BaseParser

class ExcelParser(BaseParser):
    """
    Parses Excel spreadsheet files (.xlsx) into record dictionaries
    compatible with the schema inference engine.
    """
    def __init__(self, max_file_size: int = None):
        """
        Initialize the Excel parser with an optional file size constraint.
        
        Args:
            max_file_size (int, optional): Maximum size threshold in bytes.
        """
        super().__init__(max_file_size)

    def parse(self, file_path: str):
        """
        Reads the primary worksheet of an Excel workbook and converts it to
        a list of dictionaries.
        
        Args:
            file_path (str): Filesystem path to the Excel workbook.
            
        Returns:
            List[Dict[str, Any]]: Normalized record dictionaries.
        """
        # Step 1: Validate file size safety bounds
        self.validate_file(file_path)

        # Step 2: Read first worksheet into a pandas DataFrame using openpyxl
        # Only the first sheet is read (pandas default sheet_name=0).
        df = pd.read_excel(file_path, engine='openpyxl')

        # Step 3: Transform tabular rows into list of dictionaries
        return df.to_dict(orient='records')
