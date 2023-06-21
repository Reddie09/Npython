"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas
Sua função é inverter o iterável
A função reversed() retorna um iteravel chamado list reverse iterator
"""
# Exemplos

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla ou conjunto
print(list(reversed(lista)))

# No set não se define ordem!
print(set(reversed(lista)))

print(tuple(reversed(lista)))

# Podemos iterar sobre o reversed
for letra in reversed('Reddie Nine'):
    print(letra, end='')

print('\n-')
# podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Reddie Nine'))))
