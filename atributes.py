from bs4 import BeautifulSoup
with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

# o acesso a atributos em python sao apartir de decionarios, passandoa chave e o valor da tag
print('showing class from tag ', soup.p['class'])
print('showing atributes from ', soup.p.attrs)
print('showing atributes from a tag', soup.a['href'])
print(soup.a.get('href'))
