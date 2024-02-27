import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            return f"file {file_path} deleted"
        else:
            return "no write access."
    else:
        return "file does not exist"

file_path = 'C:\Visual Studio Code\PP2\PP2\PP2\C.txt'
print(delete_file(file_path))
