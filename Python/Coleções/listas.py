"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICOS e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
     - Possuem tamanho e tipo de dado fixo
     Ou seja, nestas linguaguens se você criar um array do tipo int e com tamanho 5, este array
     será SEMPRE do tipo inteiro e poderá ter SEMPRE no máximo 5 valores.

Python
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes : []

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

#OBS: Com append, só é possível adicionar 1 elemento por vez
#lista1.append(12, 34, 56) > ERRO

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend((123, 44, 67)) # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista1 = lista1 + lista2
# lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista utilizando o reverse

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o último elemento de uma lista
# O pop não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5) 

# Podemos remover um elemento pelo índice
# OBS: Os elementos à direita desse índice serão deslocados a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos de uma lista (zerar uma lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # É possível especificar o separados, no caso a vírgula
print(curso)

# Convertendo uma lista em uma string

lista6 = ('Programação', 'em', 'Python:', 'Essencial')
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e trasnforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6 e coloca um "$" entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)
"""

print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n',
          'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 7865839747]
print(lista6)
