"""
Filter

filter -> serve para filtrar dados de uma determinada coleção
"""
# Biblioteca para trabalhar com estatistica
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizados
media = statistics.mean(dados)

# Obs: assim como a função map, a filter() recebe dois parametros, uma função e um iterável

res = filter(lambda x: x > media, dados)
print(list(res))
# Assim como a função map, após serem utilizados os dados de filter, eles são excluídos da memória

paises = ['', 'Argentina', '', 'Brasil', 'Chile', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
res = filter(None, paises)
print(list(res))

# Exemplo mais complexo

users = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro Pizzas"]},
    {"username": "carlos", "tweets": ["Eu adoro gatos"]},
    {"username": "jeff", "tweets": []},
    {"username": "bobby", "tweets": ["Eu adoro farofa", "Eu adoro Cerveja"]},
    {"username": "llr0", "tweets": ["Eu adoro bolos", "Eu adoro Pizzas", "Eu adoro Xis"]},
    {"username": "doggo", "tweets": []},
    {"username": "rex", "tweets": []},
]

# Filtrar os usuários inativos
print(users)

inativos = list(filter(lambda u: len(u["tweets"]) == 0, users))

print(inativos)

# combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome
# tenha menos de 5 caracteres

lista = (list(map(lambda nome: f'Sua instrutora é: {nome}',
                  filter(lambda nome: len(nome) < 5, nomes))))
print(lista)
