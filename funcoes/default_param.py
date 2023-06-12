"""
Funções com parâmetro padrão

- funções onde a passagem de parâmetro é opcional
"""


def exp(num0, pot=2):
    return num0 ** pot


print(exp(4, 3))

# Se o usuário passar somente um argumento, este será atribuido ao parâmetro número
# Se o usuário passar dois argumentos, este será atribuidos ao numero e potência

# Em funções python, os valores default DEVEM sempre estar ao final da declaração


def mostra_info(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo Instrutor'
    elif nome == 'Geek':
        return 'Eu Não sou o Instrutor'
    return f'Olá {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Ozzy'))

# Escopo - Para evitar problemas...
# Variáveis Globais e locais

instrutor = 'Geek'
# Global


def diz_oi():
    # instrutor = 'Python'
    return f'oi {instrutor}'


# Caso use variável local com o mesmo nome de uma variável global, a local terá preferência
print(diz_oi())

total = 0


def incr():
    global total
    total = total + 1
    return total
