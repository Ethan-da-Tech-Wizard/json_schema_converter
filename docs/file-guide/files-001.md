# Files 1 of 1 — Universal JSON Schema Converter

[All pages](../FILE_GUIDE.md) · [Project guide](../PROJECT_GUIDE.md)

| File | Role and useful details |
| --- | --- |
| [.DS_Store](../../.DS_Store) | Binary resource for .DS Store; 8,196 bytes. |
| [.github/workflows/python-app.yml](../../.github/workflows/python-app.yml) | GitHub Actions workflow for python app; defines automation triggers, jobs, and build/check steps. |
| [.gitignore](../../.gitignore) | Defines local data, credentials, dependencies, and generated outputs that Git should leave untracked. |
| [LICENSE](../../LICENSE) | Preserved license, copyright, or attribution terms; read the full text before reusing the covered component. |
| [LOG.md](../../LOG.md) | Documentation: Universal JSON Schema Converter: Action & Logic Log. Covers Project Metadata; Action Log; [2026-06-14] - Phase 1: Foundation & Initialization. |
| [PROJECT_NOTES.md](../../PROJECT_NOTES.md) | Preserved detailed setup, usage, architecture, and development notes from the earlier README. |
| [README.md](../../README.md) | Project overview, current status, entry points, setup navigation, and documentation links. |
| [TECHNICAL_MANUAL.md](../../TECHNICAL_MANUAL.md) | Documentation: Universal JSON Schema Converter: Ultimate Technical Manual. Covers 1. Environmental Setup & Security; Command: `python3 -m venv venv && source venv/bin/activate`; Command: `pip install -r requirements.txt`. |
| [core/.DS_Store](../../core/.DS_Store) | Binary resource for .DS Store; 6,148 bytes. |
| [core/engine.py](../../core/engine.py) | Shared Core Engine with Type Safety and Robust Error Handling. Defines `InferenceError`, `SchemaEngine`. |
| [core/parsers/.DS_Store](../../core/parsers/.DS_Store) | Binary resource for .DS Store; 6,148 bytes. |
| [core/parsers/base.py](../../core/parsers/base.py) | Base Parser Class for the Universal JSON Schema Converter. Rationale: Every file format (CSV, XML, etc.) needs to be normalized into a standard Python object (dict or list) before… Defines `SecurityError`, `ParsingError`, `BaseParser`. |
| [core/parsers/csv_parser.py](../../core/parsers/csv_parser.py) | CSV Parser Implementation with Memory Optimization. Rationale: For massive CSVs, we use chunking to avoid loading the entire file into RAM at once. This is a "Senior-Tier" optimiza… Defines `CSVParser`. |
| [core/parsers/excel_parser.py](../../core/parsers/excel_parser.py) | Excel (XLSX) Parser Implementation. Rationale: Excel files are binary and multi-sheet. We use `pandas` with the `openpyxl` engine to read the first sheet by default and convert it… Defines `ExcelParser`. |
| [core/parsers/json_parser.py](../../core/parsers/json_parser.py) | JSON Parser Implementation. Rationale: While JSON is already "structured," we pass it through a parser to ensure it is valid before it hits the inference engine. This maintains a c… Defines `JSONParser`. |
| [core/parsers/xml_parser.py](../../core/parsers/xml_parser.py) | XML Parser Implementation. Rationale: XML is a tree-based format. To infer a JSON Schema, we must first "flatten" it into a Python dictionary. `xmltodict` is the industry standard… Defines `XMLParser`. |
| [core/parsers/yaml_parser.py](../../core/parsers/yaml_parser.py) | YAML Parser Implementation. Rationale: YAML is a human-friendly superset of JSON. By using `yaml.safe_load`, we ensure that we don't execute any arbitrary code embedded in the YAML… Defines `YAMLParser`. |
| [docs/DEPENDENCIES.csv](../../docs/DEPENDENCIES.csv) | Machine-readable inventory of declared and locked dependencies, versions, reported licenses, and evidence URLs. |
| [docs/FILE_GUIDE.md](../../docs/FILE_GUIDE.md) | Index of the complete tracked-file guide, with one entry for every file and links to the paginated descriptions. |
| [docs/LICENSE_REVIEW.md](../../docs/LICENSE_REVIEW.md) | Original-code license, preserved component notices, dependency-license evidence, and unresolved distribution questions. |
| [docs/PROJECT_GUIDE.md](../../docs/PROJECT_GUIDE.md) | Maintainer orientation: purpose, important entry points, source layout, commands, and project-specific boundaries. |
| [docs/file-guide/files-001.md](../../docs/file-guide/files-001.md) | One page of the tracked-file catalog; links each listed path to its role and source-derived details. |
| [documents/ARCHITECTURE.md](../../documents/ARCHITECTURE.md) | Documentation: Architecture Diagram & Flow. Covers 1. High-Level Flow (Mermaid); 2. Component Breakdown. |
| [documents/FRD.md](../../documents/FRD.md) | Documentation: Functional Requirements Document (FRD). Covers 1. Interface Options; 2. Input Handling; 3. Parsing & Normalization. |
| [documents/PRD.md](../../documents/PRD.md) | Documentation: Product Requirements Document (PRD). Covers 1. Executive Summary; 2. Target Audience; 3. User Stories. |
| [documents/PROBLEM_STATEMENT.md](../../documents/PROBLEM_STATEMENT.md) | Documentation: Problem Statement: The Universal JSON Schema Gap. Covers Context; The Problem; Goal. |
| [documents/REPO_STRUCTURE.md](../../documents/REPO_STRUCTURE.md) | Documentation: Repository Structure Plan. |
| [documents/RISK_REGISTER.md](../../documents/RISK_REGISTER.md) | Documentation: Risk Register. |
| [documents/SCOPE_AND_MILESTONES.md](../../documents/SCOPE_AND_MILESTONES.md) | Documentation: Scope Lock & Milestones. Covers 1. In-Scope; 2. Out-of-Scope; 3. Milestones. |
| [documents/SRD.md](../../documents/SRD.md) | Documentation: System Requirements Document (SRD). Covers 1. Software Environment; 2. Hardware Requirements; 3. Deployment. |
| [documents/STRATEGY.md](../../documents/STRATEGY.md) | Documentation: Project Strategy: The "Why". Covers Core Value Proposition; Top 3 Real-World Use Cases; 1. The "Data Quality Policeman". |
| [extension/.DS_Store](../../extension/.DS_Store) | Binary resource for .DS Store; 6,148 bytes. |
| [extension/package-lock.json](../../extension/package-lock.json) | Dependency lockfile recording resolved package versions and integrity/source metadata; update through the project’s package manager. |
| [extension/package.json](../../extension/package.json) | Node package manifest for json-schema-converter; scripts: vscode:prepublish, compile, watch; declares package dependencies and metadata. |
| [extension/src/extension.ts](../../extension/src/extension.ts) | Source module for extension; defines `runs`, `activate`, `deactivate`. |
| [extension/tsconfig.json](../../extension/tsconfig.json) | Structured tsconfig data; top-level fields: `compilerOptions`, `exclude`. |
| [requirements.txt](../../requirements.txt) | Python dependency requirements and optional dependency groups; install with the project’s documented interpreter and environment. |
| [scripts/run.py](../../scripts/run.py) | Standalone Execution Script (run.py). Rationale: This provides a zero-boilerplate entry point. It uses a registry-style lookup to find the correct parser based on file extension, w… Defines `main`. |
| [tests/.DS_Store](../../tests/.DS_Store) | Binary resource for .DS Store; 6,148 bytes. |
| [tests/samples/.DS_Store](../../tests/samples/.DS_Store) | Binary resource for .DS Store; 6,148 bytes. |
| [tests/samples/batch_1.csv](../../tests/samples/batch_1.csv) | Tabular batch 1 data; columns: `id`, `name`, `email`, `join_date`. |
| [tests/samples/batch_2.csv](../../tests/samples/batch_2.csv) | Tabular batch 2 data; columns: `id`, `name`, `phone`. |
| [tests/samples/test.csv](../../tests/samples/test.csv) | Tabular test data; columns: `id`, `name`, `price`, `in_stock`, `category`. |
| [tests/samples/test.json](../../tests/samples/test.json) | Structured test data; top-level fields: `name`, `version`, `active`, `tags`, `metadata`. |
| [tests/samples/test.xlsx](../../tests/samples/test.xlsx) | Binary resource for test; 4,897 bytes. |
| [tests/samples/test.xml](../../tests/samples/test.xml) | Configuration or build metadata for test; read alongside the application or tool that loads it. |
| [tests/samples/test.yaml](../../tests/samples/test.yaml) | Configuration or build metadata for test; read alongside the application or tool that loads it. |
| [tests/test_engine.py](../../tests/test_engine.py) | Enterprise-grade unit tests for the SchemaEngine. Rationale: Automated testing ensures that future changes don't break existing features. Defines `test_basic_inference`, `test_strict_mode`. |
