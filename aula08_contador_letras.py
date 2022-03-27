

def contador_letras(lista_palavras):
    contador = [] # recebe uma lista
    for x in lista_palavras: # em lista de palavras
        quantidade = len(x) # mostra a quantidade
        contador.append(quantidade) # adiciona a quantidade
    return contador # retorna de modo contado do que foi passado na lista

def teste():
    return 'teste'

if __name__ == '__main__': # método principal pra que seja possível estanciar em outra classe externa
    lista = ['cachorro', 'gato'] # lista de animais
    print(contador_letras(lista)) # imprimi as letras que foram contadas
