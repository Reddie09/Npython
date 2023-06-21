"""
Any e All

All() - retorna True se todos os elementos do iterável são verdadeiros,
ou ainda se o iterável está vazio.

any() - retorna true se  qualquer elemento iteravel for verdadeiro, se
estiver vazio, retorna false
"""
# Exemplo all
print('-All-')
print(all([0, 1, 2, 3, 4]))
# Retorna False por causa do 0
print(all([1, 2, 3, 4]))
print(all([]))
print(all({1, 2, 3, 4}))
print(all([1, 2, 3, 4]))

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']

print(all([nome[0] == 'C' for nome in nomes]))
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print('-Any-')
print(any([0, False, (), (), []]))
print(any([0, 1, 2, 3]))
