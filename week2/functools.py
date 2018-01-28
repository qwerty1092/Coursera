import functools


x = functools.reduce(lambda x, y: x * y, range(1, 6))
print(x)
