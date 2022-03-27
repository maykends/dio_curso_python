
# Método -> Não retorna valor
# Função -> Retorna valor
# Classe -> proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos anexados a ela, para manter seu estado

# def soma(a, b): # método soma, no qual retorna valor, por sua vez é uma função
#     return a + b
#
#
# def sub(a, b):
#     return a - b
#
#
# def div(a, b):
#     return a / b
#
#
# def mult(a, b):
#     return a * b
#
#
# def resto(a, b):
#     return a % b
#
#
# print('Soma: {}'.format(soma(1, 3)))
# print('Subtração: {}'.format(sub(1, 3)))
# print('Divisão: {}'.format(div(1, 3)))
# print('Multiplicação: {}'.format(mult(1, 3)))
# print('Resto: {}'.format(resto(1, 3)))








class Calculadora:

    # def __init__(self, num1, num2): # iniciliza a clase, ao inicalizar essa clase, irá passar primeiro pelo método _init_
    #   pass # o init não pode ser vazio, o pass não faz nada é apenas para não ficar vazio



    def soma (selfe, valor_a, valor_b): # Como estão dentro de uma classe, só tem acesso através do self pra que possa pegar o valor de A e B
        return valor_a + valor_b

    def sub(selfe, valor_a, valor_b):
        return valor_a - valor_b

    def div(selfe, valor_a, valor_b):
        return valor_a / valor_b

    def mult(selfe, valor_a, valor_b):
        return valor_a * valor_b

    # print('Soma: {}'.format(soma(1, 3)))
    # print('Subtração: {}'.format(sub(1, 3)))
    # print('Divisão: {}'.format(div(1, 3)))
    # print('Multiplicação: {}'.format(mult(1, 3)))
    # print('Resto: {}'.format(resto(1, 3)))

# instanciar uma classe

calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.sub(100,2))
print(calculadora.div(5,3))
print('Multiplicação: {}'.format(calculadora.mult(4,8)))
