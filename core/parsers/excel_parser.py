# Program: json_schema_converter - excel_parser.py
# Programmer: Ethan-da-Tech-Wizard (written with Claude, an AI assistant)
# Last Modified: 2026-11-18
# Purpose: Defines ExcelParser, which reads the first sheet of an .xlsx file with pandas and returns its rows as a list of dictionaries.

"""
Excel (XLSX) Parser Implementation.
Rationale: Excel files are binary and multi-sheet. We use `pandas` with the 
`openpyxl` engine to read the first sheet by default and convert it into 
the same "list of dicts" format used by our CSV parser. This maintains 
consistency across all tabular formats.
"""
# This line imports pandas to handle the tabular data in Excel
import pandas as pd
# This line imports our BaseParser class
from .base import BaseParser

# This line defines the ExcelParser class for handling modern .xlsx files
class ExcelParser(BaseParser):
    """Parser for modern Excel (.xlsx) files."""
    
    # This line allows the ExcelParser to accept a custom file size limit
    def __init__(self, max_file_size=None):
        """Pass the optional file size limit up to BaseParser."""
        # This line calls the parent (BaseParser) constructor to set the limit
        super().__init__(max_file_size)

    # This method reads an Excel sheet and turns it into a list of objects
    def parse(self, file_path: str):
        """
        Reads the first sheet of an Excel file and converts it to a list of dictionaries.
        """
        # This line runs our security check to make sure the file isn't too large
        self.validate_file(file_path)

        # This line uses pandas and the 'openpyxl' engine to read the first sheet of the Excel file
        df = pd.read_excel(file_path, engine='openpyxl')
        # This line converts the spreadsheet rows into a list of dictionaries for the schema engine
        return df.to_dict(orient='records')
