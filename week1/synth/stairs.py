#import sys
#num_steps = int(sys.argv[1])
num_steps=5
for x in range(num_steps):
    print(" "*(num_steps-x-1)+"#"*(x+1))