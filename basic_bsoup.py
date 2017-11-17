import requests
from bs4 import BeautifulSoup
'''
with open('index.html', 'r') as f:
    soup_string = BeautifulSoup( f.read(), 'html.parser' )
print(soup_string)
'''

'''
r = requests.get('http://www.googl.com')

soupt  = BeautifulSoup(r.text, 'lxml')
print(soupt)
'''

with open('index.html', 'r') as f:
    soup_string = BeautifulSoup(f.read(), 'html5lib')
    print (soup_string)
