import os

def path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return filename, directory
    else:
        return "path does not exist", None

path = 'c:\Visual Studio Code\PP2\PP2\PP2'
filename, directory = path_info(path)
print("Filename:", filename)
print("Directory:", directory)
