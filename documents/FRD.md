# Functional Requirements Document (FRD)

## 1. Interface Options
- **FR1 (VS Code):** The system MUST provide a VS Code Extension that adds a "Generate JSON Schema" option to the context menu of supported files.
- **FR2 (Script):** The system MUST provide a standalone `run.py` script that takes a file path as an argument.
- **FR3 (Shared Engine):** Both interfaces MUST use the same underlying Python-based inference engine.

## 2. Input Handling
- **FR4:** The system MUST support single file input.
- **FR5:** The system SHOULD support directory input for batch processing (Script-only in Phase 1).
- **FR6:** The system MUST detect file extensions (.json, .yaml, .yml, .xml, .csv, .xlsx).

## 3. Parsing & Normalization
- **FR7:** The system MUST convert input data into a standard Python dictionary/list format.
- **FR8:** For CSV/Excel, the system MUST infer header names as keys.
- **FR9:** For XML, the system MUST handle attributes and nested tags.

## 4. Schema Generation
- **FR10:** The system MUST use the `genson` library for schema inference.
- **FR11:** The system MUST support merging schemas from multiple data samples.
- **FR12:** The output MUST be valid JSON Schema Draft 7.

## 5. Output
- **FR13:** The system MUST output a `.json` file containing the generated schema.
- **FR14:** For the VS Code Extension, the output file SHOULD be created in the same directory as the source file with a `.schema.json` suffix.
- **FR15:** The output MUST be pretty-printed for readability.
