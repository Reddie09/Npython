"""
Dictionary Comprehention

Pense no seguinte:
    Se quisermos criar uma lista pense o seguinte:
        lista = [1, 2, 3]
    tupla:
        tupla = (1, 2, 3, 4) # 1, 2, 3, 4
    set/conjunto:
        set = {1, 2, 3, 4}
    dicionario:
        dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxe
{chave:valor for valor in iteravel}
"""
# Exemplos
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros0 = [1, 2, 3, 4, 5]

quadrado0 = {valor: valor ** 2 for valor in numeros0}

print(quadrado0)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)
