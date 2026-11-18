# Program: json_schema_converter - test_engine.py
# Programmer: Ethan-da-Tech-Wizard (written with Claude, an AI assistant)
# Last Modified: 2026-11-18
# Purpose: Pytest unit tests that check SchemaEngine infers object schemas and honors strict mode.

"""
Enterprise-grade unit tests for the SchemaEngine.
Rationale: Automated testing ensures that future changes don't break existing features.
"""
# This line imports the pytest library for running tests
import pytest
# This line imports our SchemaEngine for testing
from core.engine import SchemaEngine

# This test verifies that the engine correctly identifies a basic object
def test_basic_inference():
    """Check the inferred schema is an object with the "id" and "name" properties."""
    # This line sets up the engine
    engine = SchemaEngine()
    # This line provides sample data
    data = {"id": 1, "name": "Test"}
    # This line adds the data
    engine.add_data(data)
    # This line gets the resulting schema
    schema = engine.get_schema()
    
    # These lines "Assert" (verify) that the schema is correct
    assert schema['type'] == 'object'
    assert 'id' in schema['properties']
    assert 'name' in schema['properties']

# This test verifies that 'Strict Mode' correctly forces fields to be required
def test_strict_mode():
    """Check strict mode lists "id" in the schema's required fields."""
    # This line sets up the engine in strict mode
    engine = SchemaEngine(strict=True)
    data = {"id": 1}
    engine.add_data(data)
    schema = engine.get_schema()
    
    # This line verifies that 'id' is in the 'required' list
    assert 'id' in schema['required']
