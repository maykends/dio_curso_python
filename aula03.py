##### AND
# a = int(input('Informe o primeiro valor: '))
# b = int(input('Informe o segundo valor: '))
# c = int(input('Informe o terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do Programa')

##### AOR
# a = int(input('Informe o primeiro valor: '))
# b = int(input('Informe o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um númnero par')
# else:
#     print('nenhum número par foi digitado')

##### OR NOT

# a = int(input('Informe o primeiro valor: '))
# b = int(input('Informe o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um númnero par')
# else:
#     print('nenhum número par foi digitado')

#####

a = int(input('Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado o primeiro bimestre:'))

b = int(input('Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado o segundo bimestre:'))

c = int(input('Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado o terceiro bimestre:'))

d = int(input('Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado o quarto bimestre:'))
media = (a + b + c + d) / 4

print('Média: {}'.format(media))

#
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada')