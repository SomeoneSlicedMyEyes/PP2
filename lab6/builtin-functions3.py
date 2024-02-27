def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string
string = str(input(": "))
if is_palindrome(string):
    print("palindrome")
else:
    print("Not palindrome")
