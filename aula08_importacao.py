# módulo são arquivos em .py

# importação

from aula07_televisao import Televisao
from aula07_calculadora01 import Calculadora
from aula08_contador_letras import contador_letras, teste

televisao = Televisao()
print(televisao.ligada)
televisao.ligar()
print(televisao.ligada)

calculadora = Calculadora(5,10)
print(calculadora.soma())

lista = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista))
total_letras = contador_letras(lista)
print('Total de letras na lista : {}'.format(total_letras))

print(teste())
