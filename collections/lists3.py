"""
Listas 3 - Outros métodos
"""
# Encontrar o indice de um elemento em uma lista
num = [4, 5, 6, 5, 7, 8, 9, 10]
# Em qual indice o valor 6 está?
print(num.index(6))

# Em qual indice da lista está o valor 9?
print(num.index(9))
# Caso item não está presente na lista, apresentará erro (value error)
print(num.index(5))
# Retorna o primeiro item encontrado na lista

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(num.index(5, 2))

# Podemos fazer busca entre um range, inicio/fim
print(num.index(8, 4, 8))

# Rev Slicing
print(num[2:])
# Começando do indice 2
print(num[:2])
# Terminando em 2

# Soma
print(sum(num))
# Máximo
print(max(num))
# Minimo
print(min(num))
# Comprimento
print(len(num))

# Transformar Lista em Tupla
print(num)
print(type(num))
tup = tuple(num)
print(tup)
print(type(tup))

# Desenpacotamento de listas

list2 = [1, 2, 3]
a, b, c = list2
print(a)
print(b)
print(c)
# Se tivermos número diferente de elementos na lista ou variáveis, teremos erro

# Shallow copy e Deep Copy
list3 = list2.copy()
print(list3)
list3.append(4)
print(list3)
# Veja que ao utilizarmos list.copy() copiamos os dados da lista para uma
# outra, mas elas ficaram totalmente independentes
list4 = list2
print(list4)
list4.append(43)
print(list2)
print(list4)
# Veja que utilizamos copia via atribuição, e copiamos os dados da lista para a nova lista
# Mas após realizar modificação em uma das listas, essa modificação se refletiu em ambas
# As listas. Isso em python é chamado de Shallow Copy
