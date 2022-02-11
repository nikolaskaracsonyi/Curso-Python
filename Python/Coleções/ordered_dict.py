"""
Módulo Collections: Ordered Dict

https://docs.python.org/3/library/collections.html#collections.OrderedDict

# Em um dicionário a ordem dos elementos não é garantida.
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazendo o import

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'Chave = {chave} : Valor = {valor}')
"""

from collections import OrderedDict

# Entendendo a diferença entre Dict e OrderedDict

dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> Já que a ordem dos elementos não importa para dicionários comuns

# OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})

odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False já que no OrderedDict a ordem dos elementos importa.