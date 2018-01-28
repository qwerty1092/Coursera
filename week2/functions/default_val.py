def new(arg1='arg1'):
    print(f'Hello, {arg1}')

print(new('Artem'))

print(new())

print(new.__defaults__)

# to emphasize that there is no default use None

def new(arg1=None):
    print(f'Hello, {arg1}')