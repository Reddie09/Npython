"""
Escopo de Variáveis

Dois casos de escopo

1 - Variaveis Globais
    - Seu escopo compreende t.odo o programa
2 - Variaveis Locais
    - Seu escopo está limitado ao bloco onde foi declarada

Para declarar Variáveis em Python fazemos:
nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica, isso significa que
ao declararmos uma variavel, n colocamos o tipo de dados dela
Este tipo é inferido ao atribuirmos valor na mesma

reatribuição é possível em python
"""
# variável global
num = 43
print(num)
print(f'tipo: {type(num)}')

num = 'numero'
print(num)
print(f'tipo: {num}')

# variável local
num = 3
if num > 10:
    novo = num + 10
    print(novo)
