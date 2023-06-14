"""
Listas Aninhadas / Nested List

- Algumas linguagens de programação possuem uma estrutura de dados chamadas
de Arrays:
    - Unidimensionais (vetores)
    - Multidimensionais (matrizes)

Em Python nós temos as listas

numeros = [1, 'b', 3.4321, True, 5]
"""
# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(listas)
print(type(listas))
print('-')
# Acessando os dados
print(listas[0][1])
print('-')
# Iterando com loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

print('-')
# List comprehention
[[print(valor) for valor in lista] for lista in listas]
