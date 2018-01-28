from datetime import datetime

def get_seconds():
    """Return current seconds"""
    return datetime.now().second

print(get_seconds())
print(get_seconds().__doc__)