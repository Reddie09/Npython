"""
**kwargs

Este é só mais um parâmetro, mas diferente do *args, que cologa os valores extras
em uma tupla, o **kwargs exige que utilizemos parâmetros nomeados, e transforma
esses parâmetros extras em um dicionário
"""
# Exemplo


def cores(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores(marcos='verde', julia='vermelho', vanessa='branco')

# Obs: nem os parâmetros *args e **kwargs não são obrigatórios.
cores()
cores(red='crismon')


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento pythonico'
    elif 'geek' in kwargs:
        return f'{kwargs["geek"]} Geek!'
    return 'Não tenho certeza quem vc é'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi!'))

"""
Nas nossas funções podemos ter (Nesta ordem):
- Parâmetros obrigatórios:
- *args
- Parâmetros default (não obrigatórios)
- ** kwargs
"""


def n_func(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


n_func(9, 'Julia')
n_func(19, 'Jorge', 4, 5, 3, solteiro=True)
n_func(34, 'Red', eu='Não', você='Vai')

# Desempacotando com **kargs


def mostra_nome(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Reddie', 'sobrenome': 'Nine'}

print(mostra_nome(**nomes))


def soma_multiplos(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

soma_multiplos(*lista)
soma_multiplos(*tupla)
soma_multiplos(*conjunto)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos(**dicionario)

# Obs: os nomes das chaves de um dict devem ser o mesmos do parâmetro da função
