import time
import asyncio
import pdb
import socket


#pdb.set_trace()
class Client:
    def __init__(self,host, port, timeout=15):
        self.host=host
        self.port=port
        self.timeout=timeout
        self.timeout=15
    
   
    def put(self, key, metric_value, timestamp = int(time.time())):
        data= 'put {} {} {}\n'.format(key,float(metric_value),int(timestamp))
        with socket.create_connection((self.host,self.port),self.timeout) as sock:
            try:
                sock.sendall(data.encode())
                server=sock.recv(1024)
                if server == 'error\nwrong command\n\n':
                    raise ClientError
            except Exception:
                raise ClientError

    def get(self,key):
        msg='get {}\n'.format(key).encode()
        with socket.create_connection((self.host,self.port),self.timeout) as sock:
            try:
                sock.sendall(msg)
                data = sock.recv(4096)
                clean_data=data.decode().split('\n')[1:-2]
                new_d=dict()
                for w in clean_data:
                    metrics=w.split(' ')
                    key=metrics[0]
                    values=(int(metrics[2]),float(metrics[1]))
                    if key in new_d:
                        new_d[key].append(values)
                    else:
                        new_d[key]=[values]
                        
                return new_d
                    
            except Exception:
                print(type(Exception))
                raise ClientError
            
            
                
                
            
class ClientError(Exception):
    print("Error!")       

test=Client(10,10)
