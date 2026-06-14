# Universal JSON Schema Converter: Ultimate Technical Manual

This document provides an exhaustive, line-by-line breakdown of the project's logic, commands, and senior-tier architectural decisions.

---

## 1. Environmental Setup & Security
### Command: `python3 -m venv venv && source venv/bin/activate`
- **Execution:** Creates an isolated "bubble" for Python.
- **Why:** Prevents system-wide conflicts. Modern macOS requires this (PEP 668) to protect the OS.
### Command: `pip install -r requirements.txt`
- **Execution:** Downloads Genson, Pandas, PyYAML, xmltodict, and openpyxl.
- **Why:** These are the "heavy lifting" libraries that allow us to convert complex data into JSON structures.

---

## 2. Core Architecture: The "Parser Registry"
### File: `core/parsers/base.py`
- **The Switch:** `MAX_FILE_SIZE` defaults to 1GB.
- **Logic:** `if self.max_file_size == 0: return` -> This is the "Unlimited Toggle." If you set it to 0, the safety switch is flipped off.
- **Why:** Provides "Safe by Default, Flexible by Command" security.

### File: `scripts/run.py`
- **The Registry:** `parsers = { '.csv': CSVParser(), ... }`
- **Logic:** Instead of complex `if/else` blocks, we use a dictionary to "lookup" the right tool for the job. 
- **Why:** Adding a new format like `.parquet` would only take one line of code here.

---

## 3. High-Performance Logic (Enterprise Tier)
### Memory Optimization (CSV Chunking)
- **Logic:** `pd.read_csv(file_path, chunksize=10000)`
- **Execution:** Instead of swallowing a 5GB file at once, the code "nibbles" it 10,000 rows at a time.
- **Why:** Protects against "Out of Memory" crashes on standard workstations.

### Batch Merging (Master Schema)
- **Logic:** `if os.path.isdir(input_path): ... engine.add_data(data)`
- **Execution:** The script loops through every file in a folder and feeds them into the SAME engine.
- **Why:** Creates a "Master Blueprint" that covers every variation across an entire dataset.

---

## 4. The VS Code Bridge (Safety First)
### File: `extension/src/extension.ts`
- **The Change:** Switched `exec` to `spawn`.
- **Logic:** `spawn(venvPython, [pythonScript, filePath])`
- **Execution:** Pass-by-parameter. The computer never "reads" the filename as a command.
- **Why:** Prevents "Shell Injection" attacks where a malicious file name could delete your hard drive.

---

## 5. Reliability & Observability
### Logging (The "Black Box")
- **Logic:** `logger.info("Generating final JSON Schema")`
- **Why:** Replaces "silent" prints with a traceable record. In a professional setting, these logs are used to debug failures in real-time.

### CI/CD (GitHub Actions)
- **Logic:** `.github/workflows/python-app.yml`
- **Why:** Automatically runs `pytest` every time you save your work. It acts as a "Guardian" that prevents broken code from being published.

---

## 6. Type Safety & Custom Errors
### Type Hinting
- **Logic:** `def add_data(self, data: Union[Dict, List]) -> None:`
- **Why:** Tells the computer exactly what type of data to expect. It makes the code 10x easier to read for other developers and helps VS Code catch bugs before you even run the code.

### Exception Hierarchy
- **Logic:** `class ParsingError(Exception): pass`
- **Why:** Precise failure reporting. You'll know if the error was a "Security Problem," a "File Format Problem," or an "Inference Problem."
