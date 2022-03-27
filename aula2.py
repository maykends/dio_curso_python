
a = int(input('Entre com o primeiro valor: ')) # convetendo para int
b = int(input('Entre com o segundo valor: ')) # convetendo para int
print(type(a))

# a = 10
# b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# print(type(soma)) # Saída int
# soma = str(soma)  # conversão de int para String
# print(type(soma)) # Saída String
# print('Soma: {}'.format(soma))
# print('Soma: {}. Subtração: {}'.format(soma, subtracao))
#ou
resultado = 'Soma: {soma}. ' \
            '\nsubtracao: {subtracao}'\
            '\nmultiplicacao: {multiplicacao}'\
            '\ndivisao: {divisao}'\
            '\nresto: {resto}'.format(soma =soma,
                                subtracao = subtracao,
                                multiplicacao = multiplicacao,
                                divisao = divisao,
                                resto = resto)

print(resultado)


# print('Soma: ' + str(soma)) # Saída String junto ao somatório entre a + b
# print(type(soma)) # Saída String
# #print("Soma = ", + soma) # Saída normal da soma entre a + b
#
#
# print("Subtração = ", + subtracao)
#
# print("Multiplicacao = ", + multiplicacao)
#
# print("Divisão = ", + divisao)
# print(type(divisao)) # Saída do tipo float
# print(int(divisao))  # Remove a casa decimal 2.0 para apenas 2
#
# print("Reto da Divisão = ", + resto)


# x = '1'
# soma2 = int(x) + 1 # converte String para Int. Assim podemos somar as duas variáveis
# print("Somatório", + soma2) # Saída: 'Somatório 2'