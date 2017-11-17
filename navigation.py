from bs4 import BeautifulSoup

with open('arquivo02.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

print(soup.title)
print(soup.head.title)
print(soup.a)
