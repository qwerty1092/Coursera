def extender(source, extendr):
    source.extend(extendr)

val = [1,2,3]
extender(val,[4,5])

print(val)   #lists can be changed itself inside the function

#if we try tuple:

def extender(source_tuple, extendr):
    source_tuple.extend(extendr)


val1 = (1, 2, 3)
extender(val1, (4, 5))

print(val1)  # lists can be changed itself inside the function


###it's best behaviour