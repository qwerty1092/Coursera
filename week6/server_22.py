import os
import json
import tempfile
import asyncio

st_path = os.path.join(tempfile.gettempdir(),'new7.data')
    
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
        text=message.split(' ')
        server_data=get_data()
        msg=''
        if text[0]=='put':
            if len(text)==4:
                new_val=([text[2],text[3][0:-1]])
                if text[1] in server_data:
                    if new_val not in server_data[text[1]]:
                        server_data[text[1]].append(new_val)
                else:
                    server_data[text[1]]=[new_val]
                msg='ok\n'
            else:
                msg='error\nwrong command\n'
                
            with open(st_path, 'w') as f:
                    f.write(json.dumps(server_data))      
        elif text[0]=='get':
            msg='ok\n'
            if text[1][:-1] in server_data:
                for values in server_data[text[1][:-1]]:
                    val1=str(values[0])
                    val2=str(values[1])
                    msg=msg+text[1][:-1]+' '+val1+' '+val2+'\n'
                msg=msg+'\n'
            elif text[1][:-1]=='*':
                for key in server_data:
                    for values in server_data[key]:
                        val1=str(values[0])
                        val2=str(values[1])
                        msg=msg+key+' '+val1+' '+val2+'\n'

        
        else:
            msg='error\nwrong command\n'
            
        msg=msg+'\n'
        self.transport.write(msg.encode())   

run_server('127.0.0.1', 8888)
