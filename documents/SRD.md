# System Requirements Document (SRD)

## 1. Software Environment
- **Runtime:** Python 3.9 or higher (Tested on 3.14).
- **OS:** Windows 10+, macOS 12+, Ubuntu 20.04+.
- **Dependencies:** 
  - `genson`: Schema inference.
  - `pandas`: Tabular data parsing.
  - `xmltodict`: XML processing.
  - `PyYAML`: YAML processing.
  - `openpyxl`: Excel support.

## 2. Hardware Requirements
- **CPU:** Any modern dual-core processor.
- **RAM:** Minimum 512MB (increased for large file parsing, e.g., 2GB+ for massive CSVs).
- **Disk:** < 100MB for installation.

## 3. Deployment
- **Method:** Source code execution or bundled executable via `PyInstaller`.
- **Environment Variables:** None required for core functionality.
