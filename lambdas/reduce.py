"""
Reduce

OBS: A partir do Python 3+ a função reduce() não é mais build-in
temos que importar esta função a partir do módulo 'functools'

Para entender o reduce()

Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# e você tem uma função que recebe dois parâmetros:

def func(x, y):
    return x * y

assim como map() e filter() a função reduce() recebe dois parâmetros: dados e função

a função reduce(), funciona da seguinte forma:
    passo1: res1 = f(a1, a2)
Aplica a função nos dois primeiros elementos e guarda o resultado
    passo 2: res 2 = f(res1, a3)
Aplica a função no passo 1 e mais o 3o elemento e guarda o resultado
e isso é aplicado até o final
ou seja, a cada passo ela aplica a função passando como primeiro argumento o resultado
da aplicação anterior, no final reduce() irá retornar o resultado final
"""
# Exemplo - Usando reduce() para multiplicar todos elementos de uma lista
from functools import reduce

dados = [2, 3, 4, 5, 6, 7, 8, 9]
# Para usar o reduce() precisamos duma função que recebe dois parâmetros
res = reduce(lambda x, y: x * y, dados)
print(res)

# Faezndo o mesmo com loop normal
res = 1
for n in dados:
    res = res * n

print(res)
