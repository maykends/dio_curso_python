
# classe personalizada de Exception
class Error(Exception):
    pass # usa-se o pass para que possa ser usada

class InputError(Error):  ### classe erda de Error
    def __init__(self, message): # Cria-se um construtor
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10:
            raise InputError('Nota não pode ser maior que 10') # força uma excecao
        elif x <0:
            raise input('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)