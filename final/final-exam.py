import argparse
import requests
import bs4
import json
import socket

def main():
    parser = argparse.ArgumentParser(description='final exam script')
    parser.add_argument('-ip', dest='ip', type=str, metavar='[ip address]', required=True, help='ip address')
    parser.add_argument('-f',  dest='f', type=int, metavar='[function #]', required=True, help='function to call (1-5)')
    args = parser.parse_args()

    if args.f > 5 or 1 > args.f:
        print(f'Invalid arguments: -f needs to be on or between 1 and 5')
        exit()

    URL = f'http://{args.ip}/q{args.f}'

    print('Name: Arthur Sommer')
    print(URL)
    if args.f == 1:
        print(f'Answer: {get_response(URL)}')
    elif args.f == 2:
        print(f'Answer: {parse_string(URL)}')
    elif args.f == 3:
        print(f'Answer: {parse_header(URL)}')
    elif args.f == 4:
        print(f'Answer: {parse_json(URL)}')
    elif args.f == 5:
        print(f'Answer: {socket_client(args.ip)}')
    else:
        print('Invalid')


def get_response(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f'There was a problem connecting to {url}: {exc}')
        exit()
    return response.text

def parse_string(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f'There was a problem connecting to {url}: {exc}')
        exit()
    return bs4.BeautifulSoup(response.text, 'html.parser').select('h3')[0].getText()

def parse_header(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f'There was a problem connecting to {url}: {exc}')
        exit()
    return response.headers.get('MATC-HEADER')

def parse_json(url):
    response = requests.get(url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print(f'There was a problem connecting to {url}: {exc}')
        exit()
    respDict = json.loads(response.text)
    music_and_books = respDict.get('Music And Books')
    for item in music_and_books:
        if item.get('title') == '1984':
            returnValue = item.get('author')
    return returnValue

def socket_client(ip):
    data = ''
    for port in range(5000, 6001):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        try:
            sock.connect((ip, port))
            sock.send('secret'.encode('ascii'))
            data = sock.recv(1024)
            sock.close()
        except socket.error as e:
            sock.close()
    return data.decode('ascii').strip()

if __name__ == '__main__':
    main()
