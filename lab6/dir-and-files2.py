import os

def check_access(path):
    access = {
        'Existence': os.path.exists(path),
        'Readability': os.access(path, os.R_OK),
        'Writability': os.access(path, os.W_OK),
        'Executability': os.access(path, os.X_OK)
    }
    return access

path = 'c:\Visual Studio Code\PP2\PP2\PP2'
access = check_access(path)
print(access)
