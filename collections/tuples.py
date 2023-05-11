"""
Tuplas - tuples

Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças básicas
1 - tuplas são representadas por !vírgulas!

2 - as tuplas são imutaveis, isso significa
ao criar a tupla, ela não muda, toda a operação
em uma tupla, gera uma nova tupla
"""
print(type(()))
# A tupla é representada por (), mas veja:
tuple1 = (1, 2, 3, 4, 5, 6)
print(tuple1)

tuple2 = 1, 2, 3, 4, 5, 6, 7
print(tuple2)
print(type(tuple2))

tuple3 = (3)
# Isso não é uma tupla
print(type(tuple3))

tuple4 = (4,)
print(tuple4)
print(type(tuple4))

# Podemos gerar uma tupla dinamicamente com range
tuple5 = tuple(range(11))
print(tuple5)

# Desenpacotamento de tupla
tuple6 = ('Geek', 'Programação')
escola, curso = tuple6
print(escola)
print(curso)

# Valor soma, máximo, valor minimo e tamanho (mesmo de listas)
# Contatenação funciona igual também
# TUPLAS SÃO IMUTÁVEIS, só podemos sobreescrever os valores
for n in tuple1:
    print(n)

for index, val in enumerate(tuple1):
    print(index, val)

# Devemos usar tuplas sempre que não precisarmos modificar os dados contidos

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezenbro')
print(meses[5])

# Por que utilizar tuplas?
# - Tuplas são mais rápidas que listas
# - Tuplas deixam seu código mais seguro
# - Na tupla não temos o problema de Shallow copy
