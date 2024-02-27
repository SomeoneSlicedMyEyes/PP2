def copy_file(source_path, destination_path):
    with open(source_path, 'r') as source_file:
        with open(destination_path, 'w') as destination_file:
            for line in source_file:
                destination_file.write(line)

source_path = 'C:\Visual Studio Code\PP2\PP2\PP2\A.txt'
destination_path = 'C:\Visual Studio Code\PP2\PP2\PP2\B.txt'
copy_file(source_path, destination_path)
