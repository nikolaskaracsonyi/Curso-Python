"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datatypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionário, contendo como chave o elemento da lista passado como parâmetro e como valor a
quantidade de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrências

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})

"""

from collections import Counter
import re

# Exemplo 3

texto = """ Foca foi a primeira classe naval de submarinos operados pela Marinha do Brasil. 
Era composta pelo F1, F3 e F5, submarinos projetados pelo engenheiro naval Cesare Laurenti 
e construídos em La Spezia, Itália. A classe fazia parte do programa naval da marinha de 1906
para aquisição de navios de guerra com o intuito de modernizá-la. Os submarinos foram 
adquiridos para servirem como plataforma de treinamento e manutenção para as tripulações, 
com poucas ações navais no decorrer dos 19 anos em que estiveram ativos."""

palavras = texto.split()
#print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(10))