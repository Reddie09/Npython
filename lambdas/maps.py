"""
Maps

Função valor - diferente de map de dict

Fazemos mapeamento de valores para função
"""
import math


def area(r):
    """ Calcula a area de um circulo com raio 'r' """
    return math.pi * (r ** 2)


print(area(2))
print(area(3.2))

raios = [2, 5, 7, 44, 21.3, 10]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2, utilizando maps map é uma função que
# recebe dois parâmetros, primeiro a função, depois um iterável
areas = map(area, raios)

print('-')
print(areas)
print(type(areas))
print(list(areas))
print(areas)
print('-')
# Forma 3, map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Obs: após utilizar a função map() pela primeira vez ele é zerado
"""
Para fixar - Map

temos dados iteráveis: dados a1, a2, a3, ..., an

temos uma função: f(x)

utilizamos a função map(f, dados) onde map irá mapear cada elemento dos dados
e aplicar a função
"""
cidades = [('Berlin', 29), ('Cairo', 44), ('Tokyo', 27), ('LA', 22), ('NY', 24)]
print(cidades)
# f = 9/5 * c + 32
# Lambda

# c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))
