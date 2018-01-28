e_set=set()
num_set = {1,2,3}

#hashed lists, stored unmutable objects unsorted, unique objects to store , but set is mutable

print(2 in num_set)

#odd or even set
odd_set=set()
even_set=set()

for i in range(1,11):
    if i%2:
        odd_set.add(i)
    else:
        even_set.add(i)
print(even_set)
print(odd_set)

#operations
union_set=odd_set|even_set
intersect_set=union_set & odd_set
difference_set = union_set - odd_set
print("union: " , union_set)
print("intersect: " , intersect_set)
print("difference: " , difference_set)


#unmutable set
frozen = frozenset()