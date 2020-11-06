import selectors
import socket
sel = selectors.DefaultSelector()
host = '127.0.0.1'  # The server's hostname or IP address
port = 12286        # The port used by the server
lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # starts socket details
lsock.bind((host, port)) # binds
lsock.listen() # listens
print('listening on', (host, port)) # says where listening
lsock.setblocking(False) # non blocking mode
sel.register(lsock, selectors.EVENT_READ, data=None) # sets up socket to work with selectors
# data keeps track of sent data and recieved data
def accept_wrapper(sock):
    conn, addr = sock.accept()  # Should be ready to read
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]
# event loop
while True:
    events = sel.select(timeout=None) # blocks until sockets are readyaaaaaaa
    #  returns a list of (key, mask) for each socket
    # key is a selector keya for matching data and contains
    # a file obja attribute
    # mask is an event mask is a mask of operations which are ready
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj) # then we knoew its listening from the socket and we need to accept() it
            # our own wrapper that gets the new socket and registers it with the selecotr
        else:
            service_connection(key, mask)
            # if not none then it is known that its been accpeted abnd it needs to be serviced
            # key and mask contain everything requiredd to operate on the socket
            # 