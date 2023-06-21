"""
Min e Max

max() -> retorna o maior iterável ou o maior de dois ou mais elementos
min() -> retorna o menor valor iterável ou de dois ou mais elementos
"""
# Exemplos Max

lista = [1, 5, 4, 99, 34, 128]
print(max(lista))
# Funciona para dict, list, tupla, conjunto
print(max(3, 34))

# Faça um programa que receba dois valores do usuarios e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(max(val1, val2))

val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))

print(min(val1, val2))

nomes = ['Arya', 'Tim', 'Caramuru', 'Oliver']
print(max(nomes))
print(min(nomes))

print(max(nomes, key=lambda nome: len(nome)))
print(min(nomes, key=lambda nome: len(nome)))
