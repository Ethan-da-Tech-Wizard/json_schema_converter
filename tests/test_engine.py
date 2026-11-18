# ==============================================================================
# Program: test_engine.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Unit tests for SchemaEngine inference functionality.
#          Tests basic property inference, JSON schema structure compliance,
#          and strict mode required field enforcement.
# ==============================================================================

import pytest
from core.engine import SchemaEngine

def test_basic_inference():
    """
    Verifies that the engine correctly infers JSON schema properties and types
    from basic dictionary input.
    """
    # Step 1: Initialize schema engine in standard mode
    engine = SchemaEngine()
    
    # Step 2: Feed sample data dictionary
    data = {"id": 1, "name": "Test"}
    engine.add_data(data)
    
    # Step 3: Retrieve and validate generated schema
    schema = engine.get_schema()
    assert schema['type'] == 'object'
    assert 'id' in schema['properties']
    assert 'name' in schema['properties']

def test_strict_mode():
    """
    Verifies that enabling strict mode properly marks all discovered properties
    in the schema as required.
    """
    # Step 1: Initialize schema engine with strict=True
    engine = SchemaEngine(strict=True)
    
    # Step 2: Feed test object
    data = {"id": 1}
    engine.add_data(data)
    
    # Step 3: Verify required property list
    schema = engine.get_schema()
    assert 'id' in schema['required']
