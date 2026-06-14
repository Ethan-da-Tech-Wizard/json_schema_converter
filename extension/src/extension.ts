import * as vscode from 'vscode';
// This line imports spawn from child_process for safer background execution than exec
import { spawn } from 'child_process';
import * as path from 'path';

/**
 * Extension entry point.
 * Rationale: The extension acts as a thin UI layer. It captures the file path from 
 * the context menu and spawns the Python core engine to perform the heavy lifting.
 */
// This function runs when the VS Code extension is activated
export function activate(context: vscode.ExtensionContext) {
    // This line registers a new command that can be triggered from the context menu
    let disposable = vscode.commands.registerCommand('json-schema-converter.generate', async (uri: vscode.Uri) => {
        // This block checks if the user actually right-clicked a file
        if (!uri) {
            // This line shows an error popup in VS Code
            vscode.window.showErrorMessage('Please right-click a file in the explorer.');
            return;
        }

        // This line gets the absolute path of the file you clicked on your computer
        const filePath = uri.fsPath;
        // This line gets the folder where the extension is installed
        const extensionRoot = context.extensionPath;
        
        // This line builds the path to our Python 'run.py' script
        const pythonScript = path.join(extensionRoot, '..', 'scripts', 'run.py');
        // This line builds the path to our private Python 'venv' executable
        const venvPython = path.join(extensionRoot, '..', 'venv', 'bin', 'python3');

        // This block shows a "loading" progress bar in the bottom right of VS Code
        vscode.window.withProgress({
            location: vscode.ProgressLocation.Notification,
            title: "Generating JSON Schema...",
            cancellable: false
        }, async (progress) => {
            // This returns a "Promise" which tells VS Code to wait for the Python script to finish
            return new Promise((resolve, reject) => {
                // This line prepares the arguments for the Python script as a list of strings
                // This is safer than a single string because it prevents shell injection attacks
                const args = [pythonScript, filePath];
                
                // This line spawns the Python process with a 30-second timeout to prevent hangs
                const child = spawn(venvPython, args, { timeout: 30000 });
                
                // This line stores any text that comes out of the Python script (success messages)
                let stdout = '';
                // This line stores any error text that comes out of the Python script
                let stderr = '';

                // This block captures normal text output from Python
                child.stdout.on('data', (data) => stdout += data);
                // This block captures error text output from Python
                child.stderr.on('data', (data) => stderr += data);

                // This block runs when the Python process finishes
                child.on('close', (code) => {
                    // This block handles errors if the Python script fails (code 0 means success)
                    if (code !== 0) {
                        // This line shows an error popup with the reason for failure
                        vscode.window.showErrorMessage(`Conversion failed: ${stderr || 'Unknown error'}`);
                        // This tells the promise that the task failed
                        reject(new Error(stderr));
                        return;
                    }
                    
                    // This line predicts where the schema file was saved
                    const schemaPath = `${filePath}.schema.json`;
                    // This line shows a success popup in the bottom right
                    vscode.window.showInformationMessage(`Success! Schema created: ${path.basename(schemaPath)}`);
                    
                    // This block tells VS Code to open the newly created file so you can see it
                    vscode.workspace.openTextDocument(schemaPath).then(doc => {
                        // This line actually makes the file visible in the editor
                        vscode.window.showTextDocument(doc);
                    });
                    
                    // This tells the promise that the task is complete
                    resolve(stdout);
                });

                // This block handles errors where the Python script can't even start
                child.on('error', (err) => {
                    vscode.window.showErrorMessage(`Failed to start Python: ${err.message}`);
                    reject(err);
                });
            });
        });
    });

    // This line adds our new command to the list of things VS Code should keep track of
    context.subscriptions.push(disposable);
}

// This function runs if the extension is disabled
export function deactivate() {}
