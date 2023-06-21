"""
ZIP

zip() => cria um iteravel chamado zip object que agrega elementos de cada um
dos iteráveis passados com entrada em pares
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

print(list(zip1))

zip1 = zip(lista1, lista2)
print(tuple(zip1))

zip1 = zip(lista1, lista2)
print(set(zip1))

zip1 = zip(lista1, lista2)
print(dict(zip1))

# o ZIP utiliza o menor tamanho em iteralvel, isso significa, irá parar
# quando os elementos do primeiro iterável acabar
lista3 = [7, 8, 9, 10, 11]
zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos iterar diferentes tipos de iteraveis com zip
tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14}
zt = zip(tupla, lista, dicionario.values())
print(list(zt))

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))

p1 = [70, 81, 83]
p2 = [98, 89, 52]
alu = ['maria', 'pedro', 'carla']
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alu, p1, p2)}
print(final)
# Podemos utilizar o map para isso
final = zip(alu, map(lambda nota: max(nota), zip(p1, p2)))
print(dict(final))
