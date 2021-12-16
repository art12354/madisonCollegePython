import argparse
import socket

parser = argparse.ArgumentParser(description='file transfer client')

parser.add_argument('-f', '--filename', dest='filename', required=True, help='filename of file to send to server')

args = parser.parse_args()

try:
    f = open(args.filename, 'r')
except:
    print('An error occured while trying to open the file. Does the file exist?')
    exit()
contents = f.read().encode('ascii')
f.close()


C_SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    C_SOCK.connect(('127.0.0.1', 50001))
except:
    print('An error occured while trying to connect to the file server. Is the server running?')
    exit()
C_SOCK.send(contents)

