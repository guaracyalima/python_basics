from bs4 import BeautifulSoup
with open('arquivo03.html', 'r') as f:
    soup =  BeautifulSoup(f, 'lxml')

    tag_list = soup.find_all(['ul', 'div'])

    print(tag_list)
