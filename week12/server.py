import socket

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind(('127.0.0.1', 5000))

while(1):
    L_SOCK.listen(1)
    print('waiting for connection...')
    L_CONN, addr = L_SOCK.accept()
    print('connected!')
    while(1):
        RCV_DATA = L_CONN.recv(1024)

        if not RCV_DATA:
            break
        
        message = RCV_DATA.decode('ascii')
        if(message == 'exit'):
            L_CONN.sendall(RCV_DATA)
            continue

        print(f'recieved data: {RCV_DATA.decode("ascii")}')
        L_CONN.sendall(RCV_DATA)
    
    L_CONN.close()
