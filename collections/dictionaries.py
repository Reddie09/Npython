"""
Dicionários

OBS: em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas

Dicionários são coleções do tipo chave/valor
são representados por chaves
ps: Chaves e Valores são separados por : 'chave:valor'
    Tanto chave quanto valor pode ser quaisquer tipo de dados
    Podemos misturar tipos de dados
"""
# Criação de dicionários - Forma 1
pais = {'Br': 'Brasil', 'EUA': 'Estados Unidos da América', 'Uy': 'Uruguay'}
print(pais)
print(type(pais))

# Forma 2
paises = dict(br='Brasil', eua='Estados Unidos', uy='Uruguay')
print(type(paises))

# Acessando Elementos
# Forma 1 - Acessando via Chave
print(pais['Br'])
# Forma 2 - Via get
print(pais.get('Br'))
print(pais.get('Ru'))

paisS = pais.get('ru', 'não encontrado')
print(f'{paisS}')

print('Br' in pais)
if 'Ru' in pais:
    russia = pais['Ru']

# Podemos utilizar qualquer tipo de dado como chaves de dicionários
localidades = {
    (35.8734, 39.1324): 'Escritorio',
    (40.8734, 22.1324): 'Casa'
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}

# Forma 1
receita['abr'] = 200
print(receita)

# Forma 2 - mais comum
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário Forma 1
receita['mai'] = 150
print(receita)

# Forma 2
receita.update({'mai': 200})
# A forma de adicionar elementos ou de atualizar dados em um dicionário é a mesma
# Em dicionários !não podemos ter chaves repetidas!

# Remoção de dados em um dicionário
# Forma 1 - Mais comum
print(receita)
# OBS1: Obrigatório sempre informar a chave, e caso não encontre o elemento
# um key error é retornado
ret = receita.pop('mar')
print(ret)
print(receita)
# OBS2: Ao removermos um objeto, o valor deste objeto é sempre retornado
# Forma 2
del receita['fev']
print(receita)
# Se a chave não existir, será gerado um keyError
# Carrinho de compras
# Poderíamos utilizar lista? sim
carrinho = []

produto1 = ['PS4', 1, 2300.00]
produto2 = ['Switch', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Teríamos que saber qual é o índice de cada informação no produto
# Forma 2 - Poderíamos usar uma tupla para isso? Sim
produto1 = ('PS4', 1, 2300.0)
produto2 = ('Switch', 1, 150.0)

carrinho = (produto1, produto2)

print(carrinho)
# mesmo problema de índice
# Poderíamos usar um dicionário pra isso? Sim
carrinho = []

produto1 = {'nome': 'PS4', 'qtd': 1, 'Preço': 2300.0}
produto2 = {'nome': 'Switch', 'qtd': 1, 'Preço': 150.0}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
