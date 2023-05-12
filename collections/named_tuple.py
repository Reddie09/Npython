"""
Módulo Collections - Named Tuple

Tupla diferenciadas onde especificamos um nome para a mesma e também parâmetros
"""
from collections import namedtuple
# forma 1
doggie = namedtuple('doggie', 'idade raça nome')

# forma 2
doggie2 = namedtuple('doggie', 'idade, raça, nome')

# forma 3
doggie3 = namedtuple('cachorro', ['idade', 'raça', 'nome'])

ray = doggie(idade=2, raça='Chow', nome='Ray')

print(ray)

# Acesso de Dados
print(ray[0])
print(ray[1])
print(ray[2])

# forma 2
print(ray.idade)
print(ray.raça)
print(ray.nome)
