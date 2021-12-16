import threading
import socket


def send_data(C_SOCK, is_done_e, connected_e):

    print('waiting for connection...')

    try:
        C_SOCK.connect(('127.0.0.1', 5000))
        print(f'connection established!')
        connected_e.set()
    except socket.error as e:
        print(f'connection state: {e}')
        connected_e.set()
        is_done_e.set()
        return

    userInput = input('>')
    while(userInput != 'exit'):
        C_SOCK.send(userInput.encode('ascii'))
        userInput = input('>')
    is_done_e.set()
    C_SOCK.send(userInput.encode('ascii'))
    return

def recieve_data(C_SOCK, is_done_e, connected_e):
    connected = connected_e.wait()
    OKCYAN = '\033[96m'
    ENDC = '\033[0m'
    while(not is_done_e.isSet()):
        message = C_SOCK.recv(1024).decode('ascii')
        if(message == 'exit'):
            return
        print(f'{OKCYAN}{message}{ENDC}\n>',end='')
    return

if __name__ == '__main__':

    C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    is_done_e = threading.Event()
    connected_e = threading.Event()

    t1 = threading.Thread(target=send_data, args=(C_SOCK, is_done_e, connected_e,))
    t2 = threading.Thread(target=recieve_data, args=(C_SOCK, is_done_e, connected_e,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    C_SOCK.close()
