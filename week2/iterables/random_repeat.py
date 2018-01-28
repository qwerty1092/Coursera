import random

rand_set = set()
counter=0


while True:
    length = len(rand_set)
    x = random.randint(1,10)
    rand_set.add(x)
    counter+=1
    if length+1 != len(rand_set):
        print(counter, x, rand_set)
        break

#solution from coursera

rand_set_2 = set()

while True:
    new_num = random.randint(1,10)
    if new_num in rand_set_2:
        break

    rand_set_2.add(new_num)

print(len(rand_set_2)+1Pyth)