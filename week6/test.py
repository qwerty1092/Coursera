import os
import json
import tempfile
import asyncio

def run_server(host, port):
    loop = asyncio.get_event_loop()
    # Each client connection will create a new protocol instance
    coro = loop.create_server(EchoServerClientProtocol, host, port)
    server = loop.run_until_complete(coro)
    
    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    
    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
    
st_path = os.path.join(tempfile.gettempdir(),'new.data')
print(st_path)

def get_data():
        if not os.path.exists(st_path):
                return{}
        with open(st_path, 'r') as fr:
            raw_data=fr.read()
            if raw_data:
                return json.loads(raw_data)
            return{}


class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print(message)
        server_data=get_data()
        text=message.split(' ')
        print(text[0])
        msg=''
        if text[0]=='put':
            if len(text)==4:
                if text[1] in server_data:
                    server_data[text[1]].append((text[3][0:10],text[2]))
                else:
                    server_data[text[1]]=[(text[3][0:10],text[2])]
                msg='ok\n\n'
            else:
                msg='error\nwrong command\n\n'
            print(msg)
            print(server_data)
                
            with open(st_path, 'w') as f:
                    f.write(json.dumps(server_data))
                    
            self.transport.write(msg.encode())    
        if text[0]=='get':
            if text[1][:-1] in server_data:
                msg=json.dumps({text[1][:-1]:[server_data[text[1][:-1]]]})
            elif text[1][:-1]=='*':
                msg=json.dumps(server_data)
            print(msg) 
            self.transport.write(msg.encode())   

    
run_server('127.0.0.1', 8888)
