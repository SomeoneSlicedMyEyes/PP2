def multiply_nums(nums):
    from functools import reduce
    nums = [int(num) for num in nums]
    return reduce(lambda x, y: x * y, nums)

nums = list(input(": "))
result = multiply_nums(nums)
print(result)
