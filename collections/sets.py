"""
Conjuntos

Conjuntos em qualquer linguagem de programação estamos fazendo referências
a Teoria dos Conjuntos da teoria da matemática

No python, conjuntos são chamados de set

Sets não possuem valores duplicados - Sets não possuem valores ordenados
Elementos não são acessados via indice, ou seja, conjuntos não são indexados

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles, Quando não precisamos se
preocupar com chaves, valores e itens duplicados

os conjuntos SETS são referenciados são referenciados em Python com chaves
{}

Diferença entre SETS e DICT
    - Um dicionário tem chave/valor;
    = Um conjunto tem apenas valor;

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 6, 2, 8})
print(s)
print(type(s))
# Obs- Ao criar um conjunto, caso seja adicionado um valor existente
# não gerará erro, mas não adiciona valor repetido

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

if 3 in s:
    print('tem o 3')
else:
    print('não tem')

# Podemos checkar se o elemento está contido no conjunto
# Importante lembrar que além de não termos valores duplicados, não temos ordem
lst = [99, 2, 24, 43, 1, 5, 23]
s = {99, 2, 24, 43, 1, 5, 23}
tup = (99, 2, 24, 43, 1, 5, 23)
dic = {}.fromkeys([99, 2, 24, 43, 1, 5, 23], 'dict')
print(f'Dicionário: {dic}')
print(f'Lista: {lst}')
print(f'Set {s}')
print(f'Tuple: {tup}')

# Assim como t odos outros conjuntos python, podemos colocar tipos de dados misturados em SETS
s = {1, 'b', True, 44.3, 2}
print(s)
print(type(s))
for valor in s:
    print(valor)
"""
# Usos interessantes com sets
# Formulário de cadastro de visitantes
cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'São Paulo', 'Cuiaba', 'Porto Alegre', 'Porto Alegre']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, unicas temos
# Podemos utilizar o set para isso
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)
# O segundo é ignorado, por duplicidade
print(s)

# Remover - Forma 1 - Nenhum valor é retornado
s.remove(3)
# Obs: Caso o valor não seja encontrado será gerado um erro Keyerror

print(s)

# Forma 2
s.discard(4)

print(s)
# Se o valor não é encontrado não gera erro
# Copiando um conjunto para outro - Forma 1 - Deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow Copy

novo2 = s

novo2.add(4)

print(novo2)
print(s)

# Podemos remover todos os items de um conjunto
s.clear()
print(s)

# Métodos Matemáticos

estudantes_c1 = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_c2 = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos na turma 1 também estudam na turma 2
# Precisamos gerar um conjunto com nomes de estudantes únicos - Forma 1
# Union
unicos1 = estudantes_c1.union(estudantes_c2)
print(unicos1)

# Forma 2 - Utilizando o caracter pipe ( | )
unicos2 = estudantes_c1 | estudantes_c2

print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos
# Forma 1 - Utilizando intersection
ambos1 = estudantes_c1.intersection(estudantes_c2)
print(ambos1)

# Forma 2 - Utilizando ( & )
ambos2 = estudantes_c1 & estudantes_c2
print(ambos2)

# Gerar um conjunto de estudantes que fazem parte somente de uma turma
dif1 = estudantes_c1.difference(estudantes_c2)
print(dif1)

dif2 = estudantes_c2.difference(estudantes_c1)
print(dif2)

# Soma*, Max*, Min*, Tamanho
# * Se os valores forem todos inteiros ou reais
x = {1, 2, 3, 4}
print(sum(x))
print(max(x))
print(min(x))
print(len(x))
