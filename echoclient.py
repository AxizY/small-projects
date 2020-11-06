import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 12286        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # when socket fount
    s.connect((HOST, PORT)) # connect 
    s.sendall(b'Hello, world') # send hello world
    data = s.recv(1024) # how much data to recieve

print('Received', repr(data)) # prints the server's reply