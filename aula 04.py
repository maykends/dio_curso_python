
# for x in range(100):
#     print(x)

# for x in range(90, 101):
#     print(x)

# a = int(input(print('Entre com um número: ')))
# for x in range(1 , a+1):
#     resto = a % x
#     print(resto) # saida de um numero primo


# a = int(input(print('Entre com um número: ')))
#
# div = 0
# for x in range(1 , a+1):
#     resto = a % x
#     print(x, resto)
#     if resto ==0:
#         #div = div + 1
#         # ou
#         div += + 1
# if div == 2:
#     print('Número {} é primo'.format(a))
# else:
#     print('Número {} não é primo'.format(a))



#### imprimindo apenas os numneros primos de 1 a 100
# for num in range(101):
#     div = 0
#     for x in range(1 , num +1 ):
#         resto = num % x
#         # print(x, resto)
#         if resto ==0:
#             #div = div + 1
#             # ou
#             div += + 1
#     if div == 2:
#         print(num)

# Ou

# a = int(input(print('Entre com um valor: ')))
# for num in range(a + 1):
#     div = 0
#     for x in range(1 , num +1 ):
#         resto = num % x
#         # print(x, resto)
#         if resto ==0:
#             #div = div + 1
#             # ou
#             div += + 1
#     if div == 2:
#         print(num)

######################### WHILE #########################

# a = 0
# while a < 10:
#     print(a)
#     a += 1

# nota = int(input('Entre com uma nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com uma nota com nota até 10'))
# print(nota)
#






a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou errado o primeiro bimestre:'))

b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou errado o segundo bimestre:'))

c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou errado o terceiro bimestre:'))

d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou errado o quarto bimestre:'))
media = (a + b + c + d) / 4

print('Média: {}'.format(media))