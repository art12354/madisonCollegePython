import requests

response = requests.get('https://notpurple.com')

with open('my_web_file.html', 'w') as file:
    file.write(response.text)
