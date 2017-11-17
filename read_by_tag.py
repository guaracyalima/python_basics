from bs4 import BeautifulSoup
with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.title
print(tag)
print('showing tag name ',tag.name)
print('showing tag name ',tag.name)
