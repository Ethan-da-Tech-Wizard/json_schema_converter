# Scope Lock & Milestones

## 1. In-Scope
- Dual interface: VS Code Extension + Standalone Python Script.
- Parsing of JSON, YAML, XML, CSV, XLSX.
- JSON Schema Draft 7 output.
- Merging multiple files into one schema (Script path).

## 2. Out-of-Scope
- Standalone GUI (Desktop App).
- Conversion *from* JSON Schema to other formats.
- Support for binary formats (PDF, Images).

## 3. Milestones
- **M1: Foundation (Current):** Dual-path documentation and project setup.
- **M2: Core Engine:** Implementation of the Parser Registry and JSON/YAML support.
- **M3: Advanced Parsers:** Integration of XML, CSV, and Excel (Pandas).
- **M4: Standalone Script:** Implementation of `scripts/run.py` with basic merging.
- **M5: VS Code Extension:** TypeScript frontend development and Python bridge.
- **M6: Packaging:** Readying for GitHub release and VS Code Marketplace.
