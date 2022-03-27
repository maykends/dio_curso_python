# conjunto = {1, 2, 3, 4, 4, 2}   # conjunto não repete
# conjunto.add(5) # adiciona um novo elemento
# conjunto.discard(2) # remove oelemento 2
# print(conjunto)

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print('União {}'.format(conjunto_uniao))

conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intercção: {}'.format(conjunto_interseccao)) # saída será o unico que se repete entre os conjuntos

conjunto_difenca = conjunto.difference(conjunto2)
print('Diferença: {}'.format(conjunto_difenca)) # saida apenas os elementos que possuem em um determinado conjunto que o outro não tem

conjunto_diff_sometrica = conjunto.symmetric_difference(conjunto2)
print('Diferença Simétrica: {}'.format(conjunto_diff_sometrica)) # remove o que se repete entre os dois conjuntos


conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('Subconjunto: {}'.format(conjunto_subset)) # saida apenas se faz parte por completo de um determinado conjunto, a cabe dentro de b e b não cabe dentro de a

conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('Superconjunto: {}'.format(conjunto_superset)) # saída se pertence alguns de seus elementos em outro conjunto por completo



##### convertendo uma lista para conjunto para remover a duplicidade
lista = ['cachorro','cachorro','gato','gato','elefante'] # lista
conjunto_animais = set(lista) # convertendo para conjunto
print(conjunto_animais) # remove a dupicidade
lista_animais = list(conjunto_animais) # converter de volta para lista
print(lista_animais)

# lista[]
# tupla()
# conjunto{}