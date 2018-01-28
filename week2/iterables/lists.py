empty_list = []
empty_list = list()
# list is mutables

collections = ['list', 'tuple', 'dict', 'set']

for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

collections.append('OrderedDict')  # can be collections +=['NewList']
print(collections)

collections.extend(['ponyset', 'unicorndict'])
print(collections)

del collections[4]

print('; '.join(collections))  # add separator

# sort
num = [5,15,20,1,3,4,10]
print(num)
print(sorted(num))
print(num)
num.sort()
print(num)

