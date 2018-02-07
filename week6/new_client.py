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
                print(server)
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
                    #pdb.set_trace()
                    metrics=w.split(' ')
                    key=metrics[0]
                    values=(int(metrics[1]),float(metrics[2]))
                    if key in new_d:
                        new_d[key].append(values)
                    else:
                        new_d[key]=[values]
                print(new_d)        
                return new_d
                    
            except Exception:
                raise ClientError
            
            
                
                
            
class ClientError(Exception):
    print("Error!")
    
a=Client('127.0.0.1', 8888)

a.get('palm.cpu')
print('\n')
a.get('new.cpu')
print('\n')
a.get('*')
