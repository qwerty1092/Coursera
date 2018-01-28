import os
import tempfile


class File:
    def __init__(self, path):
        self.path=path
    
    def __str__(self):
        return self.path
    
    def write(self, string):
        try:
            with open(self.path, 'a') as f:
                f.write(string)
        except:
            pass
    
    def read_f(self):
        with open(self.path,'r') as f:
            return f.read()
    
    
    def __iter__(self):
        with open(self.path,'r') as f:
            self.lines=f.readlines()
            self.line_c=len(self.lines)
            self.counter=0
        return self

    
    def __next__(self):
        if self.counter==self.line_c:
            raise StopIteration
            
        res = self.lines[self.counter]
        self.counter+=1
        return res
        
    
    def __add__(self, other):
        new_f_v = self.read_f()+other.read_f()
        new_f = File(os.path.join(tempfile.gettempdir(), 'new.txt'))
        new_f.write(new_f_v)
        return new_f


        