"""
Moludo collections - Default dict

Default dict - Ao criar um dicionario utilizando-o informamos um valor default
podendo utilizar um lambda para isso. este valor será utilizado sempre que não
houver um valor definido. Caso tentamos acessar uma chave que não existe. essa
chave será criada e o valor default será atribuido.

#PS> Lambda são funções sem nome que podem ou não receber parâmetros de entrada
e retornar valores
"""
from _collections import defaultdict

d1 = defaultdict(lambda: 0)

print(d1)
