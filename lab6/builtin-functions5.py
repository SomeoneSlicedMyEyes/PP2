def all_elements_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
print(all_elements_true(tuple1))
print(all_elements_true(tuple2))
