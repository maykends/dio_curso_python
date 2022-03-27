
matricula = int(input('Informe sua matricula: '))
nome = input('Informe seu nome: ')

nota1 = int(input('Qual foi sua nota da AV1: '))
while nota1 > 10:
    nota1 = int(input('Nota inválida para AV1. Favor inserir uma nota até 10: '))

nota2 = int(input('Qual foi sua nota da AV2: '))
while nota2 > 10:
    nota2 = int(input('Nota inválida para AV2. Favor inserir uma nota até 10: '))

media = ( nota1 + nota2 ) / 2

if media >= 7:
    print('Você {}, matrícula {}, passou com média {}'.format(nome,matricula,media))
    sorteio = int(input('Você gostaria de participar do sorteio?(sim - 1 ou não - 0)'))
    if sorteio == 1:
        for x in range(100, 107):
            print('Seus números da sorte são {}'.format(x))
    else:
        print('Desejamos um abraço!')
else:
    print('Você está abaixo da média')


