# Repository Structure Plan

```text
json_schema_converter/
├── documents/               # Project documentation
├── core/                    # SHARED PYTHON ENGINE
│   ├── __init__.py
│   ├── engine.py            # Main inference logic
│   └── parsers/             # Modular parsers
│       ├── __init__.py
│       ├── base.py
│       ├── csv_parser.py
│       ├── xml_parser.py
│       └── yaml_parser.py
├── extension/               # VS CODE EXTENSION (TypeScript)
│   ├── package.json
│   ├── src/
│   │   └── extension.ts     # Bridges to core/engine.py
│   └── tsconfig.json
├── scripts/                 # STANDALONE SCRIPTS
│   └── run.py               # Simple one-click entry point
├── tests/                   # Unified test suite
│   ├── samples/
│   └── test_engine.py
├── requirements.txt         # Python dependencies
├── README.md
└── .gitignore
```
