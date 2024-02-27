def count_lines(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for line in file)

file_path = r'c:\Users\User\Documents\StarCraft II\Variables.txt'
line_count = count_lines(file_path)
print("Number of lines: ", line_count)
