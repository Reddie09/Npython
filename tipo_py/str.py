"""
Tipo String

Em python, um dado é considerado do tipo String sempre que
-Estiver entre aspas simples - 'uma string', 'True', 'a', '1345', '44.6'
-Estiver entre aspas duplas - "uma string"
-Estiver entre aspas simples triplas - '''uma string'''
-Estiver entre aspas duplas triplas
"""
nome = 'Reddie'
print(f'Tipo nome: {type(nome)}')
print(f'nome: {nome}')
nome2 = "Nine"
print(f'Tipo nome2: {type(nome2)}')
print(f'nome2: {nome2}')
nome3 = '''Caramuru'''
print(f'Tipo nome3: {type(nome3)}')
print(f'nome3: {nome3}')
nome4 = """tipo string"""
print(f'Tipo nome4: {type(nome4)}')
print(f'nome4: {nome4}')
print(f'{nome}{nome2}, \n{nome3}\n{nome4.upper()}')
print(nome.lower())
"""
Transforma em uma lista de strings
string.split()
"""
print(nome4.split())
# slice de string
print(nome4[0:5])
print(nome4.split()[1])
# [::-1] - Começa do primeiro elemento, até o ultimo, e inverta
print(nome4[::-1])
print(nome.replace('R', 'L'))
