# https://www.youtube.com/watch?v=xtdS7flpaoA
# https://www.youtube.com/watch?v=po8ZFG0Xc4Q

import socket
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1',9999))  #  192.168.1.26

server.listen(1)

while True:
    print("Waiting for connection ...")
    client, addr = server.accept()
    
    try:
        print('Connection established')
        
        data = b''
        while True:
            chunk = client.recv(1024)
            if not chunk:
                break
            data += chunk
        
        received_object = pickle.loads(data)
        print(f'Received: {received_object}')
    finally:
        client.close()
        
    
    