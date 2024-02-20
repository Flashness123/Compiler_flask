from flask import Flask, jsonify, render_template, request
import subprocess
import os
import shutil
import time

app = Flask(__name__)

def callCompiler():
    # Convert Windows path to WSL path for the cpl0 compiler and source file
    wsl_compiler_path = "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/cpl0"
    wsl_source_file_path = "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/submitted_code.pl0"

    # Execute the first command with WSL, assuming this generates a.cl0
    compile_result = subprocess.run(
        ["wsl", wsl_compiler_path, wsl_source_file_path],
        capture_output=True, text=True
    )

    # After ensuring a.cl0 is generated, convert its path for WSL
    wsl_output_file_path = "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/a.cl0"

    # Assuming you want to move a.cl0 to a specific directory before running the second command
    # Note: You must handle the moving of files within WSL-compatible paths

    # Then, if needed, run the second command with WSL, using the moved a.cl0
    # (Adjust the command as necessary for your actual requirements)
    run_result = subprocess.run(
        ["wsl", "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/r", wsl_output_file_path],
        capture_output=True, text=True
    )

    # Return the result of the relevant operation
    return run_result  # Or run_result if the second operation is the focus


def deleteFiles():
    file_to_delete = "C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/a.cl0"
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        return True
    return False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/compile', methods=['POST'])
def getUserCode():
    if request.method == 'POST':
        code = request.form['code']
        # Define a filename for the submitted code
        filename = "submitted_code.pl0"
        filepath = os.path.join('C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/', filename)

        # Save the submitted code to a file
        with open(filepath, 'w') as file:
            file.write(code)

        compile_result = callCompiler()
        # Return the compilation result
        return jsonify({
            "stdout": compile_result.stdout,
            "stderr": compile_result.stderr
        })
    else:
        return render_template('index.html')





@app.route('/compile_r4')
def compile_r4():
    filename = "r4.pl0"  # Example filename
    compilation_result = callCompiler(filename)

    # Wait for 5 seconds
    #time.sleep(5)

    # Delete specific files
    #deletion_success = deleteFiles()

    # Return the compilation result and deletion status as a JSON response
    return jsonify({
        "compilation_stdout": compilation_result.stdout,
        "compilation_stderr": compilation_result.stderr
        #"deletion_success": deletion_success
    })




if __name__ == '__main__':
    app.run(debug=True)
