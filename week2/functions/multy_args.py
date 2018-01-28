def printer(**kwargs):
    print(type(kwargs))

    for key, value in kwargs.items():
        print(f'{key}: {value}')
print(printer(a=10, b=11 ))


def foo(*args, **kwargs): pass

print(foo(1,2,3,a=10,b=12))