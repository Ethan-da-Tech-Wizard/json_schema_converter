# Risk Register

| ID | Risk | Impact | Probability | Mitigation Strategy |
|:---|:---|:---|:---|:---|
| R1 | Large File Memory Exhaustion | High | Medium | Use streaming parsers or Pandas chunking for massive CSVs. |
| R2 | Malformed XML/JSON | Medium | High | Robust try-except blocks with clear user error messages. |
| R3 | Schema Collision | Low | Medium | Utilize GenSON's native merging logic to handle conflicting types by promoting to 'anyOf'. |
| R4 | Cross-Platform Path Issues | Low | Low | Exclusively use Python's `pathlib` for all file operations. |
| R5 | Dependency Hell | Medium | Low | Use a virtual environment and strict versioning in `requirements.txt`. |
| R6 | AI Hallucinations in Code | Medium | High | Human-in-the-loop (Developer) review of all AI-generated logic. |
