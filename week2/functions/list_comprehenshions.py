square_list = [number**2 for number in range(10)]
print(square_list)  #replace of FOR loop

#can take conditions
square_list2 = [number**2 for number in range(10) if number%2==0]
print(square_list2)  #replace of FOR loop

#for dictionaries


square_dict={num: num ** 2 for num in range(5)}
print(square_dict)


#zip concat lists
new_list = list(zip(square_list,square_list2))
print(new_list)