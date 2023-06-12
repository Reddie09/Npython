"""
Documentando funções com docstrings
"""
# Exemplos


def diz_oi():
    """ Uma Função Simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(diz_oi())

print(diz_oi.__doc__)
# Podemos ter acesso a uma documentação de uma função em python utilizando __doc__


def expo(num0, pot=2):
    """
    Função que retorna por padrâo o quadrado de número ou número a pot informada
    :param num0: Número que desejamos gerar o exponencial
    :param pot: Potência que queremos gerar o exponencial. padrão = 2
    :return: Retorna o exponencial de número por potência
    """

    return num0 ** pot


print(expo.__doc__)