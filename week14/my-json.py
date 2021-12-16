import argparse
import requests
import json

parser = argparse.ArgumentParser(description='ip info')
parser.add_argument('-ip', dest='ip', required=True, help='ip address')
args = parser.parse_args()

url = f'http://ipinfo.io/{args.ip}/json'
jsonResponse = requests.get(url)
dictResponse = json.loads(jsonResponse.text)
for x in dictResponse:
    print(f'{x}: {dictResponse[x]}')
