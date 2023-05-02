"""
Continuação listas
"""
list1 = [1, 23, 18, 91, 4, 28, 1, 20, 3]

list2 = ['G', 'r', 'e', 'e', 't', 'i', 'n', 'g', 's']

list3 = []

list4 = list(range(11))

list5 = list('Reddie Nine')

# Podemos remover todos os elementos da lista
print('Clear')
print(list5)
list5.clear()
print(list5)

# Podemos facilmente repetir elementos em uma lista
print('multiplicação de elementos')
list1 = list1 * 3
print(list1)

# Podemos facilmente converter uma string para uma lista
print('split')
c = 'Programação em Python'
print(c)
c = c.split()
print(c)

# Convertendo lista em String
print('join')
c = ' '.join(c)
print(c)

# Iterando sobre listas
list6 = [1, 2.3, True, 'd', 'haha', [1, 2, 3]]
for element in list6:
    print(element)
print(type(list6))

cart = []
prod = ''
while prod != 'sair':
    prod = input('Adicione um produto ou digite "sair" para sair: ')
    if prod == 'sair':
        break
    else:
        cart.append(prod)

for prod in cart:
    print(prod)

# Criando listas com variáveis
nums = [1, 2, 3, 4, 5]
num1 = 1
num2 = 2
num3 = 3
num4 = 4
nums2 = [num1, num2, num3, num4]
print(f'{nums}, {nums2}')

# Acesso por indice
print('acesso por indice')
cores = ['verde', 'vermelho', 'azul', 'roxo']
print(cores[2])
print(cores[-3])
# De -1 a -4 é possivel percorrer a lista ao contrário

for cor in cores:
    print(cor)

i = 0
while i < len(cores):
    print(cores[i])
    i = i + 1

# Gerar indice em um for
print('indice')
for indice, cor in enumerate(cores):
    print(indice, cor)
