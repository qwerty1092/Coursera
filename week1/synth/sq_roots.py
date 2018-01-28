import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d=b**2-4*a*c
if d<0:
    print("No solution. D<0")
else:
    print(int((-b-(b**2-4*a*c)**0.5)/(2*a)))
    print(int((-b+(b**2-4*a*c)**0.5)/(2*a)))
