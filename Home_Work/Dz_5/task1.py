def gen_func(n):
    return (n for n in range(1, n + 1, 2))


odd_to_15 = gen_func(15)

print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(type((odd_to_15)))
