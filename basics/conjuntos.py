# coleção nao ordenado onde nao podem exisistir dados duplicados
c = {'ze1', 'ze2', 'ze3'}

print (len(c)) #mostra o tamanho dessa lista de dados

# posso verificar se um determinado parametro existe na lista, ex:
print('ze1' in c)

# ce case sensitive
#
# posso adicionar elementos aos conjuntos:
#
c.add('zeruela')

#obedece as regras de conjuntos numericos matematicos podendo ser ralizadas as mesmas operações, ex:

c1 =  { 1,2,3,4}
c2 = { 3, 4, 5 }

#exibir elementos em comun
r = c1 & c2
print ('mostra os numeros em comun nos dois conjuntos', r)

#ou
r = c1 | c2
print ('OU', r)

#minus
r = c1 - c2
print ('minus', r)
