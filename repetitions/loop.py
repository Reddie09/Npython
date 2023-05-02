"""
Estrutura de Repetição - Loop

For - for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequência ou valor iterável
>String - "Reddie"
>Lista - {1, 3, 4, 21, 5}
>Range -(1, 10)

While - Forma geral diferente (enquanto satisfas a condição)
Break - Saindo de loops com break - Funciona como c
"""
line = '-x-x-x-x-x-'
line2 = '-_-_-_-_-_-'
# Exemplo For 1
nome = "Reddie Nine"
nome += " 123"
lista = {1, 22, 4, 32}
num = range(1, 10)

for letra in nome:
    print(letra)
print(line)

# Exemplo 2
for num in lista:
    print(num)
print(line)

# Exemplo 3
for num in range(1, 10):
    print(num)
print(line)

# Exemplo 4
for letra in enumerate(nome):
    print(letra, end=' ')
print(line)

# Exemplo 5
for num in range(1, 11):
    print('\U0001f60D' * num)
print('\n')
print(line2)

# Exemplo While 1
n = 1
while n < 10:
    print(n)
    n += 1
print(line2)

# Exemplo While 2
r = ''
while r != 'S':
    r = input("Parar? ").upper()

# Exemplo Break 1
for n1 in range(1, 11):
    if n1 == 6:
        break
    else:
        print(n1)
print('end of the loop')
# Exemplo Break 2
while True:
    comando = input("Digite n para sair: ")
    if comando == 'n':
        break

