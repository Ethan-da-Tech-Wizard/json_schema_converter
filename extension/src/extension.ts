// ==============================================================================
// Program: extension.ts
// Programmer: Ethan-da-Tech-Wizard
// Last Modified: November 18, 2026
// Purpose: VS Code extension interface for Universal JSON Schema Converter.
//          Registers explorer context menu commands, triggers background Python
//          conversion processes via child_process spawn, displays progress
//          notifications, and opens newly generated schemas in the active editor.
// ==============================================================================

import * as vscode from 'vscode';
import { spawn } from 'child_process';
import * as path from 'path';

/**
 * Extension entry point activated when registered commands are triggered.
 * 
 * @param context VS Code extension context for subscriptions and paths
 */
export function activate(context: vscode.ExtensionContext) {
    // Step 1: Register context menu command for schema generation
    let disposable = vscode.commands.registerCommand('json-schema-converter.generate', async (uri: vscode.Uri) => {
        // Guard against execution without a selected target file
        if (!uri) {
            vscode.window.showErrorMessage('Please right-click a file in the explorer.');
            return;
        }

        // Step 2: Resolve target file and python runtime paths
        const filePath = uri.fsPath;
        const extensionRoot = context.extensionPath;
        const pythonScript = path.join(extensionRoot, '..', 'scripts', 'run.py');
        const venvPython = path.join(extensionRoot, '..', 'venv', 'bin', 'python3');

        // Step 3: Display notification progress UI while Python process executes
        vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Generating JSON Schema...",
            cancellable: false
        }, async (progress) => {
            return new Promise((resolve, reject) => {
                const args = [pythonScript, filePath];
                
                // Spawn conversion child process with 30-second execution safety timeout
                const child = spawn(venvPython, args, { timeout: 30000 });
                
                let stdout = '';
                let stderr = '';

                // Accumulate output streams
                child.stdout.on('data', (data) => stdout += data);
                child.stderr.on('data', (data) => stderr += data);

                // Handle completion of conversion task
                child.on('close', (code) => {
                    if (code !== 0) {
                        vscode.window.showErrorMessage(`Conversion failed: ${stderr || 'Unknown error'}`);
                        reject(new Error(stderr));
                        return;
                    }
                    
                    // Open newly generated schema in active VS Code editor window
                    const schemaPath = `${filePath}.schema.json`;
                    vscode.window.showInformationMessage(`Success! Schema created: ${path.basename(schemaPath)}`);
                    
                    vscode.workspace.openTextDocument(schemaPath).then(doc => {
                        vscode.window.showTextDocument(doc);
                    });
                    
                    resolve(stdout);
                });

                // Handle process spawn failures
                child.on('error', (err) => {
                    vscode.window.showErrorMessage(`Failed to start Python: ${err.message}`);
                    reject(err);
                });
            });
        });
    });

    // Step 4: Register disposable subscription
    context.subscriptions.push(disposable);
}

/**
 * Cleanup routine executed when the extension is deactivated.
 */
export function deactivate() {}
