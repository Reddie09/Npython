"""
Recebendo dados do usuário

input() -> Todos dado recebido em input é do tipo string

"""
# em Python, é string quando tudo que estiver entre:
# . Aspas Simples . -> 'Red'
# . Aspas Duplas . -> "Red"
# . Aspas Simples Triplas . '''red'''
# . Aspas Duplas Triplas . """red"""

# entrada de dados
# print("qual seu nome?")
# nome = input()
nome = input('Qual seu nome? ')

# print("Qual sua idade?")
# idade = input()
idade = input('Qual sua idade? ')

# processamento

# saída de dados
# print('Seja bem-vindo(a) %s' % nome) python2.x
# print('Seja bem-vindo(a) {0}'.format(nome)) python3.x
print(f'Seja bem-vindo {nome}')

# print('você, %s tem %s anos' % (nome, idade)) python2.x
# print('Você, {0} tem {1} anos'.format(nome, idade)) python2.x
print(f'Você, {nome}, tem {idade} anos')

"""
int(idade) => cast

Cast é a 'conversão' de m tipo de dado para outro
"""
print(f'{nome} nasceu em {2023 - int(idade)}')
