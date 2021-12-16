import requests
import bs4

response = requests.get('https://notpurple.com')

try:
    response.raise_for_status
    print(f'response status code: {response.status_code}')
except Exception as e:
    print(f'There was an error: {e}')
    exit()

notpurpleSoup = bs4.BeautifulSoup(response.text, 'html.parser')

title = notpurpleSoup.select('title')
a = notpurpleSoup.select('a')

print(title[0].getText())
for tag in a:
    print(tag.getText())
