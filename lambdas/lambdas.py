"""
Utilizando Lambdas

Conhecidas como expressões Lambdas, são funções sem nome, ou seja
funções anônimas
"""
# Exemplo de função em python


def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda1
# lambda x: 3 * x + 1

# Como utilizar a expressão
# calc = lambda x: 3 * x + 1

# print(calc(4))

# Podemos ter expressões lambdas com múltiplas entradas
# nome_c = lambda nome, sobrenome: \
#     nome.strip().title() + ' ' + sobrenome.strip().title()

# print(nome_c(' Reddie', 'nInE'))

autores = ['Isaac Asimov', 'Ray Brandbury', 'Robert Heinlein', 'Arthur C. Clark',
           'Frank Hebert', 'Orson Scott Card', 'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Definindo função


def g_func_quadratica(a, b, c):
    """Retorna a função f(x) = a*x**2 + b*x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = (g_func_quadratica(2, 3, -5))

print(teste(0))
print(teste(1))
print(teste(5))
