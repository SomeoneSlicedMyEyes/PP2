def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("a: "))
b = int(input("b: "))

print(f"squares of {a} to {b}:")
for square in squares(a, b):
    print(square)
