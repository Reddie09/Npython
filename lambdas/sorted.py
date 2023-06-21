"""
Sorted

diferente de sort(), que só funciona com listas

O sorted sempre retorna uma lista com os elementos do iterável ordenados
e não altera o elemento principal
"""
# Exemplo

numeros = [5, 1, 9, 4]
print(numeros)

print(sorted(numeros))

# adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True))

# podemos utilizar o sorted() para tarefas mais complexas
users = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro Pizzas"]},
    {"username": "carlos", "tweets": ["Eu adoro gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobby", "tweets": ["Eu adoro farofa", "Eu adoro Cerveja"]},
    {"username": "llr0", "tweets": ["Eu adoro bolos", "Eu adoro Pizzas", "Eu adoro Xis"]},
    {"username": "doggo", "tweets": []},
    {"username": "rex", "tweets": []},
]

print(users)
print(sorted(users, key=lambda usuario: usuario["username"]))

# Ordenando pelo número de tweets
print(sorted(users, key=lambda usuario: len(usuario["tweets"])))

musicas = [
    {"titulo": "Thunderstruck", "tocou": 32},
    {"titulo": "Never gonna give you up", "tocou": 69},
    {"titulo": "November rain", "tocou": 54},
    {"titulo": "Murmaid", "tocou": 42},
    {"titulo": "Out of the cold", "tocou": 23},
    {"titulo": "Born to be wilde", "tocou": 133},
    {"titulo": "Ain't no sunshine", "tocou": 421},
]

print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
