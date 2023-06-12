"""
Funções com parâmetro de entrada

- Funções que recebem dados para serem processados dentro da mesma
"""
# Exemplo 1


def quadrado(num0):
    return num0 ** 2


print(quadrado(2))
print(quadrado(3))
print(quadrado(5))

# Funções podem ter N parametros de entrada, ou seja, podemos receber como
# entrada, quantos valores forem necessários


def soma(a, b):
    return a + b


print(soma(4, 23))


def mult(num1, num2):
    return num1 * num2


print(mult(4, 10))
