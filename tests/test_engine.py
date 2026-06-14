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
    # This line sets up the engine in strict mode
    engine = SchemaEngine(strict=True)
    data = {"id": 1}
    engine.add_data(data)
    schema = engine.get_schema()
    
    # This line verifies that 'id' is in the 'required' list
    assert 'id' in schema['required']
