import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped():
        res=func()
        print(res)
    return wrapped




@to_json
def get_data():
  return {
    'data': 42
  }
  
get_data(1)

