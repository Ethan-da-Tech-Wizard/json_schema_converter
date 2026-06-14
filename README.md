# Universal JSON Schema Converter

A professional-grade utility to generate valid JSON Schemas (Draft 7) from virtually any data format.

## 🚀 Two Paths to Success

This project provides two ways to generate schemas, sharing a robust Python inference engine.

### 1. VS Code Extension (Integrated)
The most seamless way to work. 
- **How to use:** Right-click any supported file (`.json`, `.csv`, `.xml`, `.yaml`, `.xlsx`) in the VS Code Explorer and select **"Generate JSON Schema"**.
- **Result:** A `.schema.json` file is created and automatically opened for you.

### 2. Standalone Script (Automation)
Perfect for CI/CD pipelines or quick local usage.
- **Usage:**
  ```bash
  source venv/bin/activate
  python scripts/run.py <your_file_path>
  ```

## 🛠 Supported Formats
- **JSON:** Native support.
- **CSV:** Tabular normalization via Pandas.
- **XML:** Hierarchical mapping (including attributes) via `xmltodict`.
- **YAML/YML:** Configuration-style support.
- **Excel (.xlsx):** Multi-row spreadsheet support.

## 🧠 Architectural Philosophy
Designed by a senior engineering mindset, this project uses a **Registry-Based Parser Pattern**. 
- **Shared Core:** All interfaces call the same Python `core/engine.py`.
- **Decoupled Parsers:** Adding a new format requires zero changes to the inference engine.
- **Audit Trail:** Every technical decision and its rationale is documented in `LOG.md`.

## 📦 Installation
1. Clone the repository.
2. Run `python3 -m venv venv`.
3. Run `source venv/bin/activate`.
4. Run `pip install -r requirements.txt`.
