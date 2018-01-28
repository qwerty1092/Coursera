import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args,**kwargs):
        res=json.dumps(func(*args,**kwargs))
        print(res)
        return res
    return wrapped




@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data()


@to_json
def new_data(a,b):
    return a, b
    
new_data(15,16)

@to_json
def get_none(empty):
    return empty

get_none(None)


