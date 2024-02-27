def count_upper_lower(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count

string = str(input(": "))
upper, lower = count_upper_lower(string)
print(": ", upper)
print(": ", lower)
