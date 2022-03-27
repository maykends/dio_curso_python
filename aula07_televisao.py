
class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def ligar(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__':

    # instaciando a classe televisao
    televisao = Televisao()

    print(televisao.ligada) # false, por contra que foi inicializada
    televisao.ligar() # acessou o método power
    print(televisao.ligada)
    televisao.ligar()
    print(televisao.ligada)



    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal : {}'.format(televisao.canal))

    televisao.diminui_canal()
    print('Canal : {}'.format(televisao.canal))
