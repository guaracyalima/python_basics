from bs4 import BeautifulSoup

with open('arquivo.html', 'r') as f:
    soup = BeautifulSoup(f, 'html5lib')

# mostr a arve formatada do arquivo HTML
#print(soup.prettify())

# retorna apenas os dados sem a estrutura HTML
print(soup.get_text())

#acess o conteudo das tag
#
print(soup.p.get_text())


# impimrindo o conteudo da tag atual
print(soup.p.b.string)
