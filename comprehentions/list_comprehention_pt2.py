"""
List Comprehention pt2

Nós podemos adicionar estruturas condicionar estruturas lógicas as nossas
List Comprehention
"""
# Exemplos
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar
# Qualquer numero par modulo de 2 é o 0 e zero em python é False. not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer numero impar retornarar true neste caso
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)

# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)