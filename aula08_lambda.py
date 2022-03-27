# lambda é uma função anonima, no qual dar para resolver em uma unica linha de código, no qual é armazenado em uma variavel

# Uma expressão lambda permite escrever funções anônimas/sem-nome usando apenas uma linha de código.

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))


soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

print(soma(5,10))
print(subtracao(5,10))

# dicionário
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
soma = calculadora['soma']
#soma = lambda a, b: a + b,
multiplicacao = calculadora['multiplicacao']
print('A soma é : {}'.format(soma(4,5)))
print('A multiplicação é: {}'.format(multiplicacao(10, 2)))