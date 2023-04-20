"""
PEP 8 - PYTHON ENCHANCED PROPOSAL

PROPOSTAS DE MELHORIAS PARA A LINGUAGEM PYTHON

ZEN OF PYTHON

import this

a ideia da pep8 é que possamos escrever códigos python de forma /pythonica/

(1) - Utilize Camel Case para nomes de Classes.


class Calculadora:
    pass


class CalculadoraCientifica:
    pass



(2) - Utilize nome em minusculo, separados por underline para funções ou variáveis.


def soma():
    pass


def soma_dois():
    pass


num = 4


num_impar = 5


(3) Utilize 4 espaços para identação. (#não use tab)


if 'a' in 'banana':
    print('tem')


(4) linhas em branco
-separar funções e definições de classe com duas linhas em branco
-metodos dentro de uma classe devem ser separados com uma unica linha em branco


(5) imports
-Imports devem ser sempre feitos em linhas separadas.


# Errado

import sys, os

# Certo

import sys
import os

#n há problemas em utilizar:

from types import StringType, Listtype

#caso tenha muitos imports de um mesmo pacote, recomenda-se:

from types import(
    StringType,
    ListType,
    SetType,
    OutroType
)

#imports devem ser colocados no topo do arquivo, logo depois quaisquer comentarios
ou docstrings e antes de constantes ou variaveis globais


(6)Espaços em expressões e instruções


#Não faça:

funcao( algo[ 1 ], { outro: 2 } )

algo (1)

#faça

funcao(algo[1], {outro: 2})

algo(1)


(7) termine sempre uma instrução com uma nova linha
"""
import this
