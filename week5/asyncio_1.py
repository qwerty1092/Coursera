import asyncio

@asyncio.coroutine
def hello_world():
    while True:
        print('Hello world!')
        yield from asyncio.sleep(1.0)
        
        