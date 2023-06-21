"""
Len, Abs, Sum, Round

len() => retorna o tamanho de um iterável (numero de elementos)
abs() => retorna o valor absoluto de um numero inteiro ou real
sum() => recebe um parametro iteravel pododendo receber um valor inicial
    #Obs: O valor inicial default = 0
round() => retorna um valor arredondado para n digito de precisão
"""
# Len exemplo
print(len('Reddie'))
print(len((1, 2, 3, 4, 5)))
print(len(range(0, 10)))

# Por debaixo dos panos, qdo ultilizamos a função len o python executa
print('Geek University'.__len__())
# dunder -> dois underlines
print('-')
# Abs exemplo
print(abs(-5))
print(abs(5))
print(abs(3.14))
print(abs(-3.14))
print('-')

# Sum exemplo
print(sum([1, 2, 3, 4, 5]))
print(sum([1, 2, 3, 4, 5], 5))
# segundo exemplo com valor inicial 5
print(sum({'a': 1, 'b': 2, 'c': 3}.values()))
print('-')

# Round exemplo
print(round(10.2))
print(round(10.1))
print(round(10.5))
print(round(10.6))
print(round(9.87953, 2))
print(round(10.412312, 2))
