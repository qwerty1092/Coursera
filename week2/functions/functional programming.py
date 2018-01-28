def squary(a):
    return a**2


print(list(map(squary, range(5))))


def is_positive(a):
    return a > 0


print(list(filter(is_positive, range(-2, 3))))


print(list(map(lambda x: x**2, range(5))))


# example number list to rows

print(list(map(lambda x: str(x), range(10))))

