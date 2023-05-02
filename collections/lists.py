"""
Listas em python funcionam como vetores e matrizes (arrays)
com a diferença de serem dinâmicos e também de podermos
colocar <qualquer> tipo de dado

- Dinâmico: Diferente de C e Java, não possui tamanho fixo
e podemos usar qualquer tipo de dado

as listas em python são representadas por colchete: []

"""
list1 = [1, 23, 18, 91, 4, 28, 1, 20, 3]

list2 = ['G', 'r', 'e', 'e', 't', 'i', 'n', 'g', 's']

list3 = []

list4 = list(range(11))

list5 = list('Reddie Nine')

# Podemos Facilmente checkar se determinado valor está contido na lista
num = int(input('Digite um número: '))
if num in list4:
    print(f'Possui {num}')
else:
    print(f'Não Possui {num}')

if 'e' in list5:
    print('Tem letra E')
else:
    print('Não tem E')

# Podemos facilmente ordenar uma lista
print('sort list 1')
list1.sort()
print(list1)
print('sort list 5')
list5.sort()
print(list5)

# Podemos facilmente contar o numero de ocorrência de um valor em uma lista
print('contagem')
print(list5.count('e'))

"""
Adicionar elementos em listas - Utilizamos a função append
Só conseguimos adicionar um elemento por vez
"""
print('append')
list1.append(42)
print(list1)
# Se adicionado como list1.append([3, 4]) será inserido a lista como um item da outra lista
# Erro - list1.append(0, 3, 20)
print('extend')
list1.extend([121, 83, 43])
# Extend funciona para mais de um dado
print(list1)

# Podemos inserir um novo elemento na lista informando a posição do índice
print('insert')
list1.insert(2, 33)
print(list1)
# O valor será inserido à esquerda

# Podemos juntar 2 listas
print('+')
list6 = list1 + list2
print(list6)

# forma reverse 1
print('reverse 1 e 2')
list6.reverse()
print(list6)

# forma reverse 2
print(list1[::-1])

# Copiar uma lista
list7 = list2.copy()
print(list7)

# Tamanho da lista - conta quantos elementos tem dentro da lista
print('len / Lenght')
print(len(list1))

# Podemos remover facilmente o ultimo elemento de uma lista
print(list1)
# pop não somente remove o último elemento, mas também o retorna
print('pop')
list1.pop()
print(list1)
# Podemos remover um elemento pelo indice
list1.pop(2)
# Os elementos a direita desse indice serão deslocados para a esquerda
print(list1)
