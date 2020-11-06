import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 12286        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() # starts socket
    with conn: # when connect start to:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) #recive anything they sent
            if not data: # if nothing sent then end socket
                break
            conn.sendall(data) # otherwise send message back to client