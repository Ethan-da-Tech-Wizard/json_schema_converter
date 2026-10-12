# Universal JSON Schema Converter

Generate JSON Schema from JSON, CSV, XML, YAML, and spreadsheets through a Python engine and VS Code extension.

**Status:** Developer tool  
**Built with:** Python, TypeScript/JavaScript, VS Code

[Project guide](docs/PROJECT_GUIDE.md) · [Every file explained](docs/FILE_GUIDE.md) · [Licenses and dependencies](docs/LICENSE_REVIEW.md)

## Start here

- [scripts/run.py](scripts/run.py) — Standalone Execution Script (run.py). Rationale: This provides a zero-boilerplate entry point. It uses a registry-style lookup to find the correct parser based on file extension, w… Defines `main`.
- [core/engine.py](core/engine.py) — Shared Core Engine with Type Safety and Robust Error Handling. Defines `InferenceError`, `SchemaEngine`.
- [requirements.txt](requirements.txt) — Python dependency requirements and optional dependency groups; install with the project’s documented interpreter and environment.

[Detailed setup, usage, and development notes](PROJECT_NOTES.md) preserve the previous project documentation.

## Repository layout

| Path | Role |
| --- | --- |
| [.github/](.github/) | GitHub workflow and contributor configuration (1 tracked entries). |
| [core/](core/) | Shared domain logic and processing (9 tracked entries). |
| [docs/](docs/) | Project documentation, decisions, and reference material (5 tracked entries). |
| [documents/](documents/) | Project-specific documents components (9 tracked entries). |
| [extension/](extension/) | Project-specific extension components (5 tracked entries). |
| [scripts/](scripts/) | Build, launch, maintenance, and verification commands (1 tracked entries). |
| [tests/](tests/) | Automated checks and test fixtures (10 tracked entries). |

## Scope and current limits

Python parsers and the editor extension share the schema-inference engine. Install the declared Python requirements before using the CLI.

## License

Original project code retains **MIT** terms in [LICENSE](LICENSE). Third-party libraries, media, data, models, and tools retain their own terms. See the [license review](docs/LICENSE_REVIEW.md) and [dependency inventory](docs/DEPENDENCIES.csv).
