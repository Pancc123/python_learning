import subprocess

#print('$ nslookup www.python.org')
print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)