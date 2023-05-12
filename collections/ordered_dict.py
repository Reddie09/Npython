"""
Módulo collections - Ordered Dict
em um dicionário a ordem de inserção dos elementos não é garantida

OrderedDict - é um dicionário que nos garante a ordem de inserção dos elementos
"""
from collections import OrderedDict
d1 = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

print(d1)

for chave, valor in d1.items():
    print(f'k {chave} : v {valor}')
