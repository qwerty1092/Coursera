f = open('filename')

text_modes=['r','w','a','r+']

f=open('filename','w')

f.write('New text')

f.close()

#r+ = read write

f.read()

#get to the beginning of the file

f.seek(0)

f.readline()  #read 1 line
f.readlines()  #read all lines, separated


#context manager

with open('filename') as f:
    print(f.read())

