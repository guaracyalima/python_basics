# abre e insere dados no arquivo
arq = open('file.txt', 'w')
arq.write('pythao e froida\n')
arq.write('curso de BS4')

#abre e imprime o arquivo
#
arq = open('file.txt', 'r')
print(arq.read())
arq.close()

# outra forma de fazer a parada acima
with open('file.txt', 'r') as f:
    print(f.read())
