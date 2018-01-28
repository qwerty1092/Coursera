import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('--key')
parser.add_argument('--value',nargs ='*')

args = parser.parse_args()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if args.value is not None:
    data={}
    try:
        with open(storage_path, 'r') as fr:
            data = json.load(fr)
    except FileNotFoundError :
        pass
            
    if args.key in data:
        data[args.key].append(args.value)
    else:
        data[args.key]=args.value
        
    #print(data)

    with open(storage_path, 'w') as f:
        json.dump(data, f)
else:
    try:
        with open(storage_path) as json_file:  
            data = json.load(json_file)
            x=data[args.key]
            print(x)
    except FileNotFoundError :
        pass


    





