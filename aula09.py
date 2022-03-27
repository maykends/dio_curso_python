
# arquivo = open('teste.txt', 'w') # cria arquivo 'w' significa escrever
# arquivo = open('teste.txt', 'a') # cria arquivo 'a' significa que o arquivo já havia sido escrito e agora, só basta atualizar
# arquivo.write('\nPrimeira linha')
# arquivo.close()
import shutil


def escrever_arquivo(texto):
    diretorio = 'C:/Users/mayke/Downloads/teste.txt' # escreve aruivo em um diretório esécífico na máquina
    arquivo = open(diretorio, 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # 'r' para leitura
    texto = arquivo.read() # ler arquivo
    print(texto) # resultado

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') # sempre que encointrar um enter, vira  um item da lista
    # print(aluno_nota)

    lista_media = []
    for x in aluno_nota:
        # print(x)
        lista_notas = x.split(',')
        # print(lista_notas)
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        # converter para interiro
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno: media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/mayke/Downloads/')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/mayke/Downloads/')




if __name__ == '__main__':
    move_arquivo('Notas.txt')
    # copia_arquivo('Notas.txt')
    # lista_media = media_notas('Notas.txt')
    # print(lista_media)
    # media_notas('Notas.txt')
    # escrever_arquivo('Primeira linha. \n')
    # aluno = 'Joao, 10, 10, 10, 10\n'
    # atualizar_arquivo('Notas.txt.', aluno)
    # atualizar_arquivo('terceira linha. \n')
    # ler_arquivo('teste.txt')