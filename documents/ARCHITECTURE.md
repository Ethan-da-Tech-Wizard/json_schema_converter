# Architecture Diagram & Flow

## 1. High-Level Flow (Mermaid)

```mermaid
graph TD
    subgraph Interfaces
        A1[VS Code Extension - TS] --> B[Shared Core Bridge]
        A2[Standalone Script - Python] --> B
    end
    
    B --> C{File Type Detector}
    C -->|CSV/XLSX| D[Pandas Parser]
    C -->|XML| E[xmltodict Parser]
    C -->|YAML| F[PyYAML Parser]
    C -->|JSON| G[Native JSON Parser]
    
    D --> H[Internal Dict Representation]
    E --> H
    F --> H
    G --> H
    
    H --> I[Schema Inferrer - GenSON]
    I --> J[JSON Schema File]
    
    J --> K[Open in VS Code / Save to Disk]
```

## 2. Component Breakdown
- **VS Code Extension (`/extension`):** TypeScript-based frontend that registers context menus and spawns the Python Core.
- **Standalone Script (`/scripts/run.py`):** Direct entry point to the Python Core for non-VS Code users.
- **Shared Core Engine (`/core`):** The Python logic that handles parsing, normalization, and schema inference.
- **Parser Registry:** Modular handlers for different file formats.
