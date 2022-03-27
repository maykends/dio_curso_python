
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

    def __init__(self, num1, num2): # iniciliza a clase, ao inicalizar essa clase, irá passar primeiro pelo método _init_
        self.valor_a = num1   # selfe referencia ao próprio objeto, ou seja inicializa um objeto
        self.valor_b = num2

    def soma \
            (self): # Como estão dentro de uma classe, só tem acesso através do self pra que possa pegar o valor de A e B
        return self.valor_a + self.valor_b

    def sub(self):
        return self.valor_a - self.valor_b

    def div(self):
        return self.valor_a / self.valor_b

    def mult(self):
        return self.valor_a * self.valor_b

    # print('Soma: {}'.format(soma(1, 3)))
    # print('Subtração: {}'.format(sub(1, 3)))
    # print('Divisão: {}'.format(div(1, 3)))
    # print('Multiplicação: {}'.format(mult(1, 3)))
    # print('Resto: {}'.format(resto(1, 3)))

# instanciar uma classe

if __name__ == '--main__':

    calculadora = Calculadora(10, 2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.div())
    print('Multiplicação: {}'.format(calculadora.mult()))
