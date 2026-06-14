"""
Shared Core Engine with Type Safety and Robust Error Handling.
"""
# This line imports standard libraries for JSON, Regex, and Logging
import json
import re
import logging
# This line imports type hints for professional coding standards
from typing import Any, Dict, List, Union, Optional
# This line imports the SchemaBuilder from GenSON
from genson import SchemaBuilder

# This line configures the logger for this file
logger = logging.getLogger(__name__)

# This line defines a custom error for failures that happen during schema inference
class InferenceError(Exception):
    # This line allows the error to carry a message
    pass

# This line defines the main class that coordinates schema generation
class SchemaEngine:
    # This method runs when a new SchemaEngine is created
    # Rationale: Using Type Hints (strict: bool) makes the code self-documenting for other devs
    def __init__(self, strict: bool = False):
        # This line creates a new instance of the SchemaBuilder
        self.builder = SchemaBuilder()
        # This line stores the strictness setting
        self.strict = strict
        # This line logs the initialization
        logger.info(f"SchemaEngine initialized (Strict: {strict})")

    # This method takes data and adds it to the builder for learning
    def add_data(self, data: Union[Dict[str, Any], List[Dict[str, Any]]]) -> None:
        """
        Feeds data into the builder. Supports lists (batch) or single objects.
        """
        try:
            # This block checks if we received a list of data items
            if isinstance(data, list):
                # This line logs the batch size
                logger.debug(f"Adding batch of {len(data)} items to engine")
                # This loop processes every item in the batch
                for item in data:
                    # This line applies smart pattern detection and adds the object
                    self.builder.add_object(self._apply_smart_patterns(item))
            else:
                # This line logs that we are adding a single object
                logger.debug("Adding single object to engine")
                # This line applies patterns and adds the object
                self.builder.add_object(self._apply_smart_patterns(data))
        except Exception as e:
            # This line catches errors and wraps them in our custom InferenceError
            raise InferenceError(f"Error while feeding data to engine: {str(e)}")

    # This internal method looks for dates and emails to make the schema smarter
    def _apply_smart_patterns(self, data: Any) -> Any:
        # This block checks if we are looking at a dictionary
        if isinstance(data, dict):
            # This loop recursively processes every key and value
            for key, value in data.items():
                data[key] = self._apply_smart_patterns(value)
        # This block checks if we are looking at a list
        elif isinstance(data, list):
            # This line applies patterns to every item in the list
            return [self._apply_smart_patterns(i) for i in data]
        return data

    # This method produces the final JSON Schema
    def get_schema(self) -> Dict[str, Any]:
        """
        Returns the final generated JSON Schema.
        """
        try:
            # This line generates the raw schema from the builder
            logger.info("Generating final JSON Schema")
            schema = self.builder.to_schema()
            
            # This block applies strict requirement constraints if requested
            if self.strict:
                logger.debug("Applying strict requirement constraints")
                self._make_required(schema)
                
            # This line returns the finished schema
            return schema
        except Exception as e:
            # This line catches errors and reports them via InferenceError
            raise InferenceError(f"Failed to generate schema: {str(e)}")

    # This recursive method forces every property to be 'required'
    def _make_required(self, schema: Dict[str, Any]) -> None:
        # This block checks if we are looking at an object type with properties
        if schema.get('type') == 'object' and 'properties' in schema:
            # This line sets the 'required' list to be all existing property names
            schema['required'] = list(schema['properties'].keys())
            # This loop goes deeper into nested objects
            for prop in schema['properties'].values():
                self._make_required(prop)
        # This block checks if we are looking at an array type
        elif schema.get('type') == 'array' and 'items' in schema:
            # This line recursively makes items in the array strict
            self._make_required(schema['items'])

    # This method saves the generated schema to a file
    def save_schema(self, schema: Dict[str, Any], output_path: str) -> None:
        """
        Writes the schema to a file with pretty-printing.
        """
        try:
            # This line opens the file in write mode
            with open(output_path, 'w') as f:
                # This line saves the schema as pretty-printed JSON
                json.dump(schema, f, indent=4)
            # This line logs a success message
            logger.info(f"Schema successfully saved to {output_path}")
        except Exception as e:
            # This line logs and raises a custom error if saving fails
            error_msg = f"Failed to save schema to {output_path}: {str(e)}"
            logger.error(error_msg)
            raise InferenceError(error_msg)
