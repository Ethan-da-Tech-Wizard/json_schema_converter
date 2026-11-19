# ==============================================================================
# Program: engine.py
# Programmer: Ethan-da-Tech-Wizard
# Last Modified: November 18, 2026
# Purpose: Shared Core Schema Engine with type safety and robust error handling.
#          Accepts parsed tabular, document, or key-value data structures (single
#          objects or batches), applies pattern detection, builds cumulative
#          JSON schemas via GenSON, and applies optional strictness constraints
#          forcing required field rules across nested properties.
# ==============================================================================

import json
import re
import logging
from typing import Any, Dict, List, Union, Optional
# GenSON does the actual inference: it merges many sample objects into one
# JSON Schema. This module only prepares input and post-processes the result.
from genson import SchemaBuilder

# Configure module-level logger for schema inference diagnostics
logger = logging.getLogger(__name__)

# Single exception type so callers need not know about GenSON/IO internals.
class InferenceError(Exception):
    """Custom exception raised when schema inference or serialization fails."""
    pass

class SchemaEngine:
    """
    Coordinates JSON schema inference across single or batch payloads.
    Wraps GenSON SchemaBuilder with domain-specific enhancements such as
    strictness constraints and robust serialization.
    """
    def __init__(self, strict: bool = False):
        """
        Initialize the schema inference engine.
        
        Args:
            strict (bool): When True, forces all discovered properties to be
                           marked as required in the generated schema.
        """
        # Step 1: Initialize underlying GenSON builder instance
        # One builder accumulates every object added, so a batch (or a whole directory)
        # produces a single merged schema.
        self.builder = SchemaBuilder()
        # Step 2: Store strictness flag governing required field enforcement
        self.strict = strict
        logger.info(f"SchemaEngine initialized (Strict: {strict})")

    def add_data(self, data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> None:
        """
        Feeds parsed input data into the builder. Accepts either a single
        dictionary or a batch list of dictionaries.
        
        Args:
            data (Union[Dict, List[Dict]]): Parsed data payload to ingest.
        """
        try:
            # Step 1: Check whether payload is a batch (list) or single object (dict)
            if isinstance(data, list):
                logger.debug(f"Adding batch of {len(data)} items to engine")
                # Step 2: Ingest each batch element sequentially into the builder
                for item in data:
                    self.builder.add_object(self._apply_smart_patterns(item))
            else:
                logger.debug("Adding single object to engine")
                # Step 3: Ingest single object with pattern transformations
                self.builder.add_object(self._apply_smart_patterns(data))
        except Exception as e:
            # Wrap standard exceptions in domain-specific InferenceError
            raise InferenceError(f"Error while feeding data to engine: {str(e)}")

    def _apply_smart_patterns(self, data: Any) -> Any:
        """
        Recursively traverses data structures to prepare objects for schema analysis.
        
        Args:
            data (Any): Arbitrary object, dictionary, or list.
            
        Returns:
            Any: Processed data structure.
        """
        # Step 1: Handle dictionary structures recursively
        if isinstance(data, dict):
            for key, value in data.items():
                # Mutates the caller's dict in place; the recursion currently returns values
                # unchanged (a hook for future pattern detection), so behaviour is unaffected.
                data[key] = self._apply_smart_patterns(value)
        # Step 2: Handle list structures recursively
        # Lists are rebuilt (not mutated) from their processed items.
        elif isinstance(data, list):
            return [self._apply_smart_patterns(i) for i in data]
        return data

    def get_schema(self) -> Dict[str, Any]:
        """
        Generates and returns the compiled JSON Schema.
        
        Returns:
            Dict[str, Any]: Standard JSON Schema dictionary.
        """
        try:
            # Step 1: Compile current accumulated state into raw JSON schema
            logger.info("Generating final JSON Schema")
            schema = self.builder.to_schema()
            
            # Step 2: Enforce strict constraints if configured
            if self.strict:
                logger.debug("Applying strict requirement constraints")
                self._make_required(schema)
                
            return schema
        except Exception as e:
            raise InferenceError(f"Failed to generate schema: {str(e)}")

    def _make_required(self, schema: Dict[str, Any]) -> None:
        """
        Recursively alters schema nodes so that all defined properties
        are listed under the 'required' attribute.
        
        Args:
            schema (Dict[str, Any]): Schema node to mutate in-place.
        """
        # Step 1: Handle object nodes containing defined properties
        if schema.get('type') == 'object' and 'properties' in schema:
            # Strict mode: every property seen in the samples becomes required, even those
            # that were absent in some records. Applied at every object level.
            schema['required'] = list(schema['properties'].keys())
            for prop in schema['properties'].values():
                self._make_required(prop)
        # Step 2: Handle array nodes containing nested items schema
        elif schema.get('type') == 'array' and 'items' in schema:
            self._make_required(schema['items'])

    def save_schema(self, schema: Dict[str, Any], output_path: str) -> None:
        """
        Serializes and writes the JSON Schema to a designated filesystem path.
        
        Args:
            schema (Dict[str, Any]): The generated JSON Schema.
            output_path (str): Target destination file path.
        """
        try:
            # Write pretty-printed JSON schema with 4-space indentation
            # Overwrites an existing file at output_path without confirmation.
            with open(output_path, 'w') as f:
                json.dump(schema, f, indent=4)
            logger.info(f"Schema successfully saved to {output_path}")
        except Exception as e:
            error_msg = f"Failed to save schema to {output_path}: {str(e)}"
            logger.error(error_msg)
            raise InferenceError(error_msg)
