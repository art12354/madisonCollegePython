import socket

L_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
L_SOCK.bind(('127.0.0.1', 50001))

i = 0

while(1):
    L_SOCK.listen(1)
    L_CONN, addr = L_SOCK.accept()
    print(f'connected by: {addr}')
    while(1):
        RCV_DATA = L_CONN.recv(1024)
        if not RCV_DATA:
            break
        print('file recieved')
        filename = 'file'+str(i)+'.txt'
        i = i + 1
        data = RCV_DATA.decode('ascii')
        print(f'saving to {filename}')
        try:
            f = open(filename, 'w')
        except:
            print(f'An error occured while trying to open {filename}')
        f.write(data)
        f.close()
    L_CONN.close()
