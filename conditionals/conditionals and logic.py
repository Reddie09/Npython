"""
Estruturas condicionais
if, else, elif
Operadores Lógicos
unários: Not
binários: And, Or, Is
"""
age = int(input('Digite sua idade: '))
p1, p2 = False
if age > 18:
    print('maior de idade')
    p1 = input('Usuário Ativo? S/N: ')
    p2 = input('Usuário Logado? S/N: ')
    if p1 == 'S':
        active = True
    else:
        active = False

    if p2 == 'S':
        loggedIn = True
    else:
        loggedIn = False

    if active and loggedIn:
        print('Usuário Ativo e Logado')
    else:
        print('Usuário Inativo ou Inválido')

elif age == 18:
    print('tem 18 anos')
    p1 = input('Usuário Ativo? S/N: ')
    p2 = input('Usuário Logado? S/N: ')
    if p1 == 'S':
        active = True
    else:
        active = False

    if p2 == 'S':
        loggedIn = True
    else:
        loggedIn = False

    if active or loggedIn:
        print('Usuário Ativo ou Logado')
    else:
        print('Usuário Inativo ou Inválido')
else:
    print('menor de idade')
    print(p1 is True)
