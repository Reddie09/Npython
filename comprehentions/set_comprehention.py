"""
Set Comprehention
Set = {1, 2, 3, 4, 5}
"""
# Exemplo
numeros = {num for num in range(1, 7)}
print(numeros)

numeros0 = {x ** 2 for x in range(10)}
print(numeros0)

# transformando em dict
numeros1 = {x: x ** 2 for x in range(10)}
print(numeros1)

letras = {letra for letra in 'Geek University'}
print(letras)
