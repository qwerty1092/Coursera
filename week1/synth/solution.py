import sys
digits = sys.argv[1]

digits=str(digits)
i, j = 0, 0
for letter in digits:
    if not letter.isdigit():
        print(f"Please correct input: {letter}")
        j=1
        break

    i+=int(letter)
if j==0:
    print(i)
