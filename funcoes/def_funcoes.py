"""
Definindo Funções

Funções são pequenos trechos de código que realizam tarefas específicas
Pode ou não receber entrada de dados e retornar saída de dados
São uteis para executar procedimentos similares por repetidas vezes

Já utilizamos várias funções desde o início
 - print()
 - len()
 - max()
 - count()
 - e muitas outras
"""
# Exemplo de utilização de funções

cor = ['verde', 'amarelo', 'vermelho', 'azul', 'roxo']

# Utilizando a função integrada do python print()
print(cor)

# Exemplo de função agregada à atributo
cor.append('rosa')

# Definindo funções
"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
onde:
nome_da_funcao -> Sempre, com letras minúsculas, e se for composto, 
separado por underline

parametros_de_entrada -> Opcionais, onde tendo mais de um, 
cada um separado por vírgula, podendo ser opcionais

bloco_da_funcao -> também chamado de corpo da função ou implementação,
é onde o processamento da função acontece

Veja que para definir a função, utilizamos a palavra reservada 'def' informando
ao python que estamos definindo uma função, e abrimos o bloco de código com
dois pontos
"""


def diz_oi():
    print('olá!')


diz_oi()


def parabens():
    print('Parabéns pra você!')
    print('Muitas felicidades')


parabens()
