"""
List Comprehention

utilizando list comprehention nós podemos gerar novas listas com dados
processados a partir de outro iterável.

# Sintaxe da List Comprehention

[ dado for dado in iterável ]
"""
# Exemplos

nums = [1, 2, 3, 4, 5]

res = [numeros * 10 for numeros in nums]

print(res)

"""
Para entender melhor o que está acontecendo, devemos dividir a expressão em
duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""


res = [numero / 2 for numero in nums]

print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in nums]

print(res)

# List comprehention vs loop

# loop
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for numero in numeros:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# com ListComprehention
print([numero * 2 for numero in numeros])

# outros exemplos
nome = 'Reddie Nine'
print([letra.upper() for letra in nome])


def cx_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


friends = ['maria', 'julia', 'pedro', 'guilherme']

print([cx_alta(friend) for friend in friends])

print([numero * 3 for numero in range(1, 10)])
