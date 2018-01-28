import  random


num = random.randint(0,101)
while True:
    ans = input("Enter your number: ")
    if not ans or ans=="exit":
        break
    if not ans.isdigit():
        print("Enter correct num!")
        continue
    user_ans = int(ans)

    if user_ans>num:
        print("It's smaller")
    elif user_ans<num:
        print("It's bigger")
    else:
        print("Correct!!!")
        break