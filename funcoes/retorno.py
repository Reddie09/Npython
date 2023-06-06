"""
Funções com retorno

Quando uma função em python não retorna nenhum valor, o retorno é none
Funções que retornam valores devem retornar eles com a palavra reservada
return

return
- ela finaliza a função, ou seja, sai da função
- podemos ter, em uma função, podemos ter diferentes returns
- podemos em uma função, retornar qualquer tipo de dados, ou até mesmo
multiplos valores
"""
from random import random
# Exemplo de função


def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()

print(ret)

# Exemplo 2


def diz_oi():
    return 'oi!'


print(diz_oi())

# Exemplo 2


def nova_func():
    var1 = True
    if var1:
        return 4
    else:
        return 5


print(nova_func())

# Exemplo 3


def outra():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra()

print(num1, num2, num3, num4)

# Exemplo 4


def moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(moeda())

