def square_generator(N):
    for i in range(1, N + 1):
        yield i ** 2
N = int(input(": "))
for square in square_generator(N):
    print(square)
