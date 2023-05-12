"""
Módulo Collections - Counter
Collections -> High-Performance Container Datatypes

Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário contendo como chave o elemento da lista
passado como parâmetro e como valor a quantidade de ocorrências desse elemento
"""
# Utilizando o counter
from collections import Counter

# Podemos usar qualquer iterável
lista = [1, 1, 2, 2, 3, 3, 3, 4, 14, 14, 14]

res = Counter(lista)
print(res)
print(type(res))

# Para cada elemento da lista, ele criou uma chave e
# colocou o valor como a quantidade de ocorrencias

print(Counter('Geek University'))

texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Integer vitae facilisis nibh. Cras interdum est ut quam viverra, et 
tincidunt nisi maximus. Proin convallis congue nisl eget fermentum. 
Integer eu neque sem. Class aptent taciti sociosqu ad litora torquent 
per conubia nostra, per inceptos himenaeos. Donec condimentum velit quam, 
ut interdum lorem consectetur at. Ut vel lacus felis. Morbi luctus tempus 
enim vitae ultricies. Nunc lacinia ultrices mauris eu elementum. Nam vel 
vestibulum tortor, nec tempus turpis. Phasellus in erat in augue varius 
porttitor. Fusce blandit lacus non nibh molestie, non volutpat 
enim feugiat."""

palavras = texto.split()

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorências
print(res.most_common(5))
