"""
Tipo booleano

Algebra Booleana - George Boole

2 Constantes True or False

Sempre com a inicial Maiúscula
"""

p = True
print(f'p = {p}')

"""
Operações básicas
"""

# Negação (not)
"""
Fazendo a negação, se o valor for verdadeiro, o resultado será falso
se for falso o resultado, será verdadeiro
"""
print('#not#')
print(f'not p = {p}')

# Ou (or)
"""
É uma operação binária, ou seja, depende de dois valores, um ou outro deve ser verdadeiro
True or True = True
True or False = True
False or True = True
False or False = False
"""
print('#or#')
p1 = True
p2 = False
p3 = True
p4 = False
print(f'p1={p1}, p2={p2}, p3={p3}, p4={p4}')
print(f'p1 or p2 = {p1 or p2}')
print(f'p1 or p3 = {p1 or p3}')
print(f'p2 or p3 = {p2 or p3}')
print(f'p2 or p4 = {p2 or p4}')

# E (and)
"""
Também é uma operação binária, ou seja, depende de dois valores,
ambos valores devem ser verdadeiros
True and True = True
True and False = False
False and True = False
False and False = False
"""
print('#and#')
print(f'p1 and p2 = {p1 and p2}')
print(f'p1 and p3 = {p1 and p3}')
print(f'p2 and p3 = {p2 and p3}')
print(f'p2 and p4 = {p2 and p4}')

