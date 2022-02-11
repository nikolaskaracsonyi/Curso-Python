"""
Módulo Collections - Deque

https://docs.python.org/3/library/collections.html#collections.deque

Podemos dizer que o deque é uma lista de alta perfomance.
"""

# Fazendo o import

from collections import deque

# Criando Deques

deq = deque('geek')
print(deq)

# Adicionando elementos

deq.append('y') # Adiciona o elemento no final da lista

print(deq)

deq.appendleft('k') # Adiciona o elemento no começo da lista

print(deq)

# Removendo elementos

print(deq.pop()) # Remove e retorna o elemento do final da lista

print(deq)

print(deq.popleft()) # Remove e retorna o elemento do início da lista

print(deq)