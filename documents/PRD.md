# Product Requirements Document (PRD)

## 1. Executive Summary
A dual-access utility that accepts various file formats as input and outputs a valid JSON Schema (Draft 7+). The project provides two primary paths for users: a VS Code Extension for integrated development and a standalone Python Script for quick, scriptable execution.

## 2. Target Audience
- Data Engineers
- Backend Developers
- VS Code Power Users

## 3. User Stories
- **As a VS Code user**, I want to right-click a data file (CSV/JSON/XML) and select "Generate JSON Schema" to immediately create a schema file in my workspace.
- **As a developer**, I want a simple Python script I can run locally to convert a single file or a folder of files into schemas.
- **As a user**, I want the tool to work on Mac, Windows, and Linux.

## 4. Key Features
- **Dual Interface:** Integrated VS Code Extension + Lightweight Python Script.
- **Auto-Detection:** Automatically identify file types based on extension or content headers.
- **Recursive Merging:** Ability to "learn" from multiple files to create a robust schema.
- **Format Support:** Initial support for JSON, YAML, XML, CSV, and XLSX.

## 5. Success Metrics
- 100% valid JSON Schema output for supported formats.
- Seamless VS Code integration (right-click context menu).
- Minimal configuration for the standalone script.
