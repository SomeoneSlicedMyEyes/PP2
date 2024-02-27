import os

def directories(path):
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    return directories, files

path = 'c:\Visual Studio Code\PP2\PP2\PP2'
directories, files = directories(path)
print("Directories:", directories)
print("Files:", files)
