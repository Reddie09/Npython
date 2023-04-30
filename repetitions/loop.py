"""
Estrutura de Repetição - Loop

For - for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequência ou valor iterável
>String - "Reddie"
>Lista - {1, 3, 4, 21, 5}
>Range -(1, 10)

"""
# Exemplo For 1
nome = "Reddie Nine"
nome += " 123"
lista = {1, 22, 4, 32}
num = range(1, 10)

for letra in nome:
    print(letra)

# Exemplo 2
for num in lista:
    print(num)

# Exemplo 3
for num in range(1, 10):
    print(num)

# Exemplo 4
for letra in enumerate(nome):
    print(letra, end=' ')
    print('\n')

# Exemplo 5
for num in range(1, 11):
    print('\U0001f60D' * num)
