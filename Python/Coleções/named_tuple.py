"""
Módulo Collections - Named Tuple

https://docs.python.org/3/library/collections.html#collections.namedtuple

Recap Tupla:
tupla = (1, 2, 3)
print(tupla)

Named Tuple -> São tuplas diferenciadas, onde podemos especificar um nome para a mesma e também parâmetros.
"""

# Fazendo o import

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 -  Declarando a namedtuple (parâmetros separados por espaços)

cachorro = namedtuple('cachorro', 'idade raça nome') # namedtupla('nome_da_tupla', 'parâmetros')

# Forma 2 - Declarando a namedtuple (parâmetros separados por vírgulas)

cachorro = namedtuple('cachorro', 'idade, raça, nome')

# Forma 3 - Declarando a namedtuple (parâmetros separados em uma lista)

cachorro = namedtuple('cachorro', ['idade', 'raça', 'nome'])

# Usando

ray = cachorro(idade=2, raça='Chow-Chow', nome='Ray')
print(ray)

pisco = cachorro(idade=8, raça='Shi-tzu', nome='Pisco')
print(pisco)

cristal = cachorro(idade=5, raça='Lhasa Apso', nome='Cristal')
print(cristal)

# Acessando os dados 

# Forma 1

print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# Forma 2 - Mais fácil

print(pisco.idade) # idade
print(pisco.raça) # raça
print(pisco.nome) # nome

# Consultando índice de um valor

print(cristal.index('Lhasa Apso'))
print(cristal.count('Lhasa Apso'))