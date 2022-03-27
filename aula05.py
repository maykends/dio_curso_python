
lista = [1, 3 , 5, 7]
lista_animal = ['cachorro','gato','elefante', 'girafa', 'arara']
#print(type(lista))
#print(lista[0])

# for x in lista_animal:
#     print(x)

# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)

# print(sum(lista)) # soma da lista
# print(max(lista)) # maximo valor da lista
# print(min(lista)) # minimo valor da lista
# print(max(lista)) # letra g de gato por conta que é a mior do alfabeto


# if 'gato' in lista_animal:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um gato na lista')

# nova_lista = lista_animal * 3
# print(nova_lista)

# if 'lobo' in lista_animal:
#     print('Existe esse animal na lista')
# else:
#     print('Não existe esse animal na lista, será incl[ido')
#     lista_animal.append('lobo') # apeend add para lista
#     print(lista_animal)
#
#
# lista_animal.pop() # retira o ultimo da lista
# print(lista_animal)
#
#
# lista_animal.pop(0) # retira a posição zero
# print(lista_animal)
#
# lista_animal.remove('elefante') # remove da lista pela string
# print(lista_animal)


#### Ordenar lista

# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)

#### Reverter a lista
# lista_animal.reverse()
# print(lista_animal)

######################################## tuplas #########################################

# Qual a diferença de uma lista para uma tupla em python?
#  grande diferença é que a tupla é imutável, ou seja, após a criação não é possível realizar alterações no seu estado.

# lista_animal[0] = 'macaco'  # altera a posição zero da lista - substuindo
# print(lista_animal)


tupla = (1, 10 , 12, 14)
print(tupla)
print(tupla[0])
# tupla[0] = 12  # não é possível alterar dados em tuplas
print(len(tupla))  # conta o tanto de elementos


#### converter uma lista para uma tupla

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#### converter uma tupla  para uma lista

lista_numerica = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


