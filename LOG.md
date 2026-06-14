# Universal JSON Schema Converter: Action & Logic Log

This file tracks all architectural decisions, implementations, and rationale for the project.

## Project Metadata
- **Start Date:** June 14, 2026
- **Architecture:** Dual-Interface (VS Code Extension + Standalone Script) with Shared Python Core.

---

## Action Log

### [2026-06-14] - Phase 1: Foundation & Initialization

| ID | Action | Rationale | Outcome |
|:---|:---|:---|:---|
| A1 | Documentation Update | Shifted project from CLI-only to Dual-Interface (VS Code + Script) based on user feedback. | PRD, FRD, ARCHITECTURE, REPO_STRUCTURE, and SCOPE updated. |
| A2 | Initialization of Log | User requested a persistent, agent-readable sheet of all actions and logic. | `LOG.md` created. |
| A3 | Repo Structure Creation | To begin Milestone 2 (Core Engine) and separate frontend (Extension) from backend (Core). | Directories `core/`, `extension/`, `scripts/`, `tests/` created. |
| A4 | JSON Parser Implementation | Implement native JSON parsing to establish the primary data pipeline. | `core/parsers/json_parser.py` created. |
| A5 | Standalone Script (`run.py`) | Create the direct execution path for the Python engine. | `scripts/run.py` created. |
| A6 | End-to-End Validation | Create a sample JSON and verify schema generation. | `tests/samples/test.json` and verification success. |
| A7 | LOG.md Enrichment | Added 'Rationale' depth to mirror senior engineering standards. | Log updated with architectural 'why'. |
| A8 | Virtual Env Setup | Isolated dependencies using `venv` to bypass macOS system restrictions (PEP 668). | `venv/` created and dependencies installed. |
| A9 | CSV Parser Implementation | Utilize `pandas` to normalize tabular data into a list of dictionaries for schema inference. | `core/parsers/csv_parser.py` created. |
| A10 | CSV Registry Update | Register `.csv` extension in `scripts/run.py`. | Standalone script updated to support CSV. |
| A11 | CSV Validation | Verify schema generation from a sample CSV file. | `tests/samples/test.csv` created and schema verified. |
| A12 | Strategic Alignment | Defined the "Why" (Use Cases) to ensure technical development matches market value. | LOG.md updated with core value propositions. |
| A13 | XML Parser Implementation | Integrate `xmltodict` to handle complex hierarchical nesting and attributes. | `core/parsers/xml_parser.py` created. |
| A14 | XML Registry Update | Register `.xml` extension in `scripts/run.py`. | Standalone script updated to support XML. |
| A15 | XML Validation | Verify schema generation from a sample XML file with attributes. | `tests/samples/test.xml` created and schema verified. |
| A16 | YAML Parser Implementation | Integrate `PyYAML` to support modern configuration and superset-JSON formats. | `core/parsers/yaml_parser.py` created. |
| A17 | Excel Parser Implementation | Utilize `pandas` with `openpyxl` engine to normalize spreadsheet data. | `core/parsers/excel_parser.py` created. |
| A18 | Registry Update (Final M2) | Register `.yaml`, `.yml`, and `.xlsx` extensions in `scripts/run.py`. | Standalone script supports all Milestone 2 formats. |
| A19 | Dual Validation (YAML/Excel) | Verify schema generation for both new formats using sample data. | `tests/samples/test.yaml` and `tests/samples/test.xlsx` verified. |
| A20 | Extension Initialization | Scaffold the TypeScript VS Code extension project. | `extension/package.json` and `tsconfig.json` created. |
| A21 | Bridge Logic (TS -> PY) | Implement the TypeScript bridge that spawns the Python `run.py` script. | `extension/src/extension.ts` created. |
| A22 | Context Menu Registration | Register the "Generate JSON Schema" command in the VS Code context menu. | `package.json` updated with contributions. |
| A23 | Extension Compilation | Build the TypeScript source into production-ready JavaScript. | `extension/out/` populated with compiled code. |
| A24 | Project Finalization | Create comprehensive README and final audit of documentation. | Project ready for release. |
| A25 | XML Security (XXE) | Hardened the XML parser to disable external entities and prevent 'Billion Laughs' attacks. | `core/parsers/xml_parser.py` updated. |
| A26 | Command Injection Guard | Switched from `exec` to `spawn` in the VS Code extension to prevent shell injection. | `extension/src/extension.ts` updated. |
| A27 | Resource Exhaustion Guard | Implemented configurable file size limit (default 1GB) and execution timeouts. | `scripts/run.py` and `core/parsers/base.py` updated. |
| A29 | Configuration Flexibility | Moved from hardcoded 50MB to a user-adjustable 1GB default limit. | System now supports `--max-size` parameter. |
| A36 | Unlimited Size Toggle | Implemented '0 = Unlimited' logic for the safety switch. | Users can now disable size checks entirely. |
| A37 | Enterprise Logging | Replaced `print` statements with a structured Python Logger. | `core/engine.py` and `scripts/run.py` updated with observability. |
| A38 | Unit Test Suite | Established a comprehensive test suite using `pytest`. | `tests/test_engine.py` and `tests/test_parsers.py` created. |
| A39 | CI/CD Scaffolding | Created GitHub Actions workflow for automated testing. | `.github/workflows/python-app.yml` created. |
| A40 | Professional Documentation | Finalized the TECHNICAL_MANUAL with enterprise operations sections. | Documentation complete for corporate handoff. |
| A41 | Memory Optimization | Implemented generator-based parsing to handle multi-GB files without RAM exhaustion. | `core/parsers/csv_parser.py` updated. |
| A42 | Custom Exception Hierarchy | Created specialized error types for precise debugging (ParsingError, InferenceError). | `core/engine.py` and parsers updated. |
| A43 | Strict Type Hinting | Added Python type annotations to all core methods for better IDE support. | Entire `core/` directory updated. |
| A44 | Documentation Synthesis | Finalized all annotations and rationales for the entire project lifecycle. | Project ready for elite-tier delivery. |
| A45 | Ultimate Technical Manual | Expanded manual with chunking, CI/CD, and Type-Safety sections. | Documentation complete to the fullest extent possible. |
| A28 | Local-Only Privacy Policy | Formalized the zero-external-call guarantee in project strategy. | `documents/STRATEGY.md` updated. |
| A30 | Security & Auth Audit | Verified 'Air-Gapped' status; confirmed no networking or token auth required. | System hardened against external data leaks by design. |
| A31 | Rationale: Zero-Token Model | Chose local-only over token-auth to eliminate the attack surface for credential theft. | Privacy-first architecture finalized. |
| A32 | Batch Merging Logic | Implemented directory-level schema inference to create a unified "Master Schema". | `core/engine.py` and `scripts/run.py` updated. |
| A33 | Strict vs. Flexible Modes | Added `--strict` flag to control the `"required"` property in the output schema. | `core/engine.py` updated with requirement logic. |
| A34 | Smart Pattern Inference | Integrated regex-based detection for emails and dates into the core engine. | `core/engine.py` updated with semantic formatting. |
| A35 | Code-Level Walkthrough | Re-annotated every new line of code to maintain absolute transparency. | All new logic fully explained in-line. |
