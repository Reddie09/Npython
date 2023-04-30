"""
Ranges
Ranges são utilizados para gerar sequências numéricas,
de forma especificada
Observação, valor de parada não inclusive - inicio padrão 0
de passo 1 a 1
"""
line = '--------------'
# Exemplo 1 - somente passo final especificado
for num in range(11):
    print(num)
print(line)

# Exemplo 2 - passo inicial especificado
for num in range(3, 5):
    print(num)
print(line)

# Exemplo 3 - valor de inicio, valor de parada, passo
for num in range(2, 10, 2):
    print(num)
print(line)

# Exemplo 4 - Inversa - Valor inicio, valor de parada, passo
for num in range(10, 0, -1):
    print(num)
print(line)
