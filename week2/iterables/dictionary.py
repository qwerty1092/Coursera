empty_dict = {}
empty_dict = dict()

#key->value

#mutable

print(empty_dict.setdefault('key','default'))  #add deafault values
print(empty_dict)
print(empty_dict.setdefault('key','new_default'))

#keys can be: int, None, stings, tuples

# iterations
collection = {
    'first': ['val1', 'num1'],
    'second': ['val2', 'num2']
    }
print('iterations for keys')

for key in collection:
    print(key)

print('iteration for key: values')

for key, value in collection.items():
    print(f'{key}-{value}')

print('iteration for values')

for value in collection.values():
    print(value)


# to sort dict

from collections import OrderedDict

ordered = OrderedDict()

for num in range(10):
    ordered[num] = str(num)

for key in ordered:
    print(key)