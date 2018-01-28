import os
import json
import tempfile
import argparse




st_path = os.path.join(tempfile.gettempdir(),'new.data')

def get_data():
    
    if not os.path.exists(st_path):
        return{}
    
    with open(st_path, 'r') as fr:
        raw_data=fr.read()
        if raw_data:
            return json.loads(raw_data)
            
        return{}
        
        
def put(key,value):
    data=get_data()
    if key in data:
        data[key].append(value)
    else:
        data[key]=value
    
    with open(st_path, 'w') as f:
        f.write(json.dumps(data))
        
def get(key):
    data=get_data()
    if key in data:
        return data[key]
        
if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--key')
    p.add_argument('--value')
    args =p.parse_args()
    
    if args.value and args.key:
        put(args.key,args.value)
    else:
        get(args.key)
        
        
    
    