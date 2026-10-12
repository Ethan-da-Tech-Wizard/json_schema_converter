# Universal JSON Schema Converter

Generate JSON Schema from JSON, CSV, XML, YAML, and spreadsheets through a Python engine and VS Code extension.

**Status:** Developer tool  
**Built with:** Python, TypeScript/JavaScript, VS Code

## Reading order

1. Read the root README for project purpose and setup navigation.
2. Follow the entry points below to find the implementation.
3. Use the file guide to locate individual modules, tests, assets, and configuration.
4. Check component licenses before redistributing dependencies or assets.

## Important paths

- [scripts/run.py](../scripts/run.py) — Standalone Execution Script (run.py). Rationale: This provides a zero-boilerplate entry point. It uses a registry-style lookup to find the correct parser based on file extension, w… Defines `main`.
- [core/engine.py](../core/engine.py) — Shared Core Engine with Type Safety and Robust Error Handling. Defines `InferenceError`, `SchemaEngine`.
- [requirements.txt](../requirements.txt) — Python dependency requirements and optional dependency groups; install with the project’s documented interpreter and environment.

## Structure

| Path | Role |
| --- | --- |
| [.github/](../.github/) | GitHub workflow and contributor configuration (1 tracked entries). |
| [core/](../core/) | Shared domain logic and processing (9 tracked entries). |
| [docs/](../docs/) | Project documentation, decisions, and reference material (5 tracked entries). |
| [documents/](../documents/) | Project-specific documents components (9 tracked entries). |
| [extension/](../extension/) | Project-specific extension components (5 tracked entries). |
| [scripts/](../scripts/) | Build, launch, maintenance, and verification commands (1 tracked entries). |
| [tests/](../tests/) | Automated checks and test fixtures (10 tracked entries). |

## Scope

Python parsers and the editor extension share the schema-inference engine. Install the declared Python requirements before using the CLI.

## Maintaining the guide

The file catalog is a source-inspection snapshot, not proof that every runtime path works. Update it when moving files or changing module responsibilities. The 2026-10-12 documentation review did not run every application, deploy services, or validate all historical performance claims.
