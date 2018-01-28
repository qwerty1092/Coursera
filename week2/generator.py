def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2


ranger = even_range(2, 10)

print(next(ranger))
print(next(ranger))
print(next(ranger))
print(next(ranger))


def fibonacci(num):
    a = b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


#it's possible to get data INTO generator

# main possibility - saving of current value