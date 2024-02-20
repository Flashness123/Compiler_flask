#TODO: Ich gebe Datei an und der Pfad soll Variabel sein, der compiler Pfad soll fix sein
import os
import shutil
import subprocess
import time


def callCompiler(filename):
    filepath = f"compiler_components/{filename}"
    with open(filepath, 'r') as file:
        # Iterate over each line in the file
        contents = file.read()
        # Print the contents
        print(contents)
        file = contents



    # Run the cpl0
    result = subprocess.run(["wsl","/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/cpl0", "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/r4.pl0"], capture_output=True, text=True)

    # Output the result
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    shutil.move("C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/a.cl0","C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components")
    result = subprocess.run(["wsl","/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/r", "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/a.cl0"], capture_output=True, text=True)

    # result = subprocess.run(["wsl", "bash", "-c", "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/r", "/mnt/c/Users/Lukas/PycharmProjects/compiler_flask_app.py/a.cl0"], capture_output=True, text=True)
    #
    # # Output the result
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

def deleteFiles():
    os.remove("C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/compiler_components/a.cl0")
    #os.remove("C:/Users/Lukas/PycharmProjects/compiler_flask_app.py/a.cl0")

if __name__ == '__main__':
    filename = "r4.pl0"
    callCompiler(filename)
    print("Call delete files")
    time.sleep(1)
    #deleteFiles()

