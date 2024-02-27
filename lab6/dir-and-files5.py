def write_list_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
    print("Data has been written to", file_path)

file_path = r'c:\Users\User\Documents\StarCraft II\Variables.txt'
data = [1, 2, 3, 4, 5]
write_list_to_file(file_path, data)
