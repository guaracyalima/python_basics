from bs4 import BeautifulSoup
with open('arquivo04.html', 'r') as f:
    soup = BeautifulSoup(f, 'lxml')

tag = soup.find('li')

# print(tag)
text = soup.find(string = 'plants')

# print(text)
#
# find by id
by_id = soup.find(id = 'secondaryconsumers')
# print(by_id)

# using a function

def is_secondary_consumers(tag):
    return tag.has_attr('id') and tag.get('id') == 'secondaryconsumers'
secondary_consumer = soup.find(is_secondary_consumers)
print(secondary_consumer.li.div.string)
