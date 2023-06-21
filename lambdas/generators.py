"""
Generators

Generators -> Tuple comprehentions

"""
from sys import getsizeof
nomes = ['Carlos', 'Carmila', 'Cassiano', ]
print(any(nome[0] for nome in nomes))

# List Comprehention
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

print(getsizeof('Reddie'))
list_comp = getsizeof([x * 10 for x in range(1000)])

set_comp = getsizeof({x * 10 for x in range(1000)})

dict_comp = getsizeof({x: x * 10 for x in range(1000)})
# Gerando uma lista de numeros com generator
gen = getsizeof(x * 10 for x in range(1000))
print('Gasto de memória')
print(f'List{list_comp} bytes')
print(f'Set {set_comp} bytes')
print(f'Dict {dict_comp} bytes')
print(f'Generator Expression: {gen} bytes')

gen = (x * 10 for x in range(1000))
for num in gen:
    print(num)
