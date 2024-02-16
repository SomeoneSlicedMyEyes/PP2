def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input(": "))
even_nums_generator = even_numbers(n)

print(",".join(map(str, even_nums_generator)))
