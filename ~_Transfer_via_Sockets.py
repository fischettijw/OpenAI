# https://www.youtube.com/watch?v=xtdS7flpaoA
# https://www.youtube.com/watch?v=po8ZFG0Xc4Q

import socket
import pickle

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                       
client.connect(('127.0.0.1', 9999))   #   192.168.1.26 
# host = socket.gethostbyname(client.gethostname(socket.gethostname()))
# print(host)

try:
    myobect = {'key1': 'value1', 'key2': 'value2'}
    serialized = pickle.dumps(myobect)
    print(serialized)
    client.sendall(serialized)     # comment
finally:
    pass
    client.close()             # comment
                       