"""
Métodos para dicionários
"""
d = dict(a=1, b=2, c=3)
print(d)
print(type(d))
# Zerar dados
d.clear()
print(d)

# Copiando um dicionário de um para outro
# Forma 1 - Deep Copy
d = dict(a=1, b=2, c=3)

novo = d.copy()

novo['d'] = 4

print(d)
print(novo)

# Forma 2 - Shallow copy
d2 = dict(a=1, b=2, c=3)
n2 = d2

print(n2)

novo['d'] = 4

print(d)
print(novo)

# Forma não usual de criar dicionário
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))
# O método from keys recebe dois parâmetros: um interável e um valor
# ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta
# chave o valor informado.

# Iterar sobre dicionários
receita = {'jan': 100, 'fev': 200, 'mar': 150}
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

print(receita.keys())

# modo pythonico
for chave in receita.keys():
    print(receita[chave])

for valor in receita.values():
    print(valor)

# desempacotamento de dicionários
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

# Soma*, Valor Máximo*, Minimo*, Tamanho - * somente para numéricos
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
