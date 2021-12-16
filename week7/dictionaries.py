#1
fqdn = {
        'server1.testlab.com': '192.168.1.10',
        'server2.testlab.com': '192.168.1.11',
        'server3.testlab.com': '192.168.1.12',
        'server4.testlab.com': '192.168.1.13',
        'server5.testlab.com': '192.168.1.14',
        'server6.testlab.com': '192.168.1.15'
        }
#2
print(fqdn.keys())
#3
print(fqdn.values())
#4
print(fqdn.items())
#5
fqdn.update({
        'server7.testlab.com': '192.168.1.16',
        'server8.testlab.com': '192.168.1.17'
        })
print(fqdn.items())
#6
print(fqdn.get('server2.testlab.com'))
#7
print(fqdn.get('server10.testlab.com'))
