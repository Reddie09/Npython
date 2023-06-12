"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer, isso significa que você poderá
chamar de qualquer coisa, desde que comece com asterisco.

exemplo: xis

Mas por convenção, utilizamos *args para defini-lo

O que é *args?

o Parâmetro *args utilizado em uma função, comloca os valores extras informados
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis
"""
# Exemplos


def soma(*args):
    return sum(args)


print(soma(1, 2))


def soma2(*args):
    """
    O asterisco serve para que informemos ao python que estamos passando
    como argumento uma coleção de dados, desta forma, ele saberá que precisa
    antes desenpacotar os dados
    """
    return sum(args)


nums1 = [1, 2, 3, 2345, 0, 32.1]
print(soma2(*nums1))

