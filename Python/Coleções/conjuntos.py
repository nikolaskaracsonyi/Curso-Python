"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.

- No Python, os conjuntos são chamados de "Sets".

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são eficientes para se utilizar quando precisamos armazenar elementos mas
não nos importamos com a ordenação dos mesmos. Quando não precisamos nos preocupar com chaves, valores e itens
duplicados.

Os conjuntos (sets) são referênciados em Python com chaves ({})

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3 }) # Valores repitidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado
# sem gerar erro e não fará parte do conjunto

# Forma 2 - Mais Comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

if 3 in s:
    print('Tem o "3"')
else:
    print('Não tem o "3"')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar todos os tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}

print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes dos sets

# Imagine que desenvolvemos um formulários de cadastro de visitantes em uma feira ou museu, e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# com repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiabá', 'Campo Grande', 'São Paulo', 'Cuiabá']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? faria um loop na lista...?

# Podemos utilizar o set para isso.

print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}

s.add(4)
s.add(4) # Duplicidade não gera erro, simplesmente é ignorada e não adicionada.
print(s)

#Removendo elementos em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3) # Não é índice, informamos o valor a ser removido

print(s)

# OBS: Caso o valor não seja encontrado será gerado KeyError. Nenhum valor é retornado.

# Forma 2

s.discard(2) # Se o valor não for encontrado nenhum erro é gerado

print(s)

s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro

# Forma 1  -  Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy

novo = s
novo.add(4)

print(novo)]
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos, um contendo estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}


# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando .union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractér pipe "|"

unicos2 = estudantes_python|estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando .intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando "&"

ambos2 = estudantes_python&estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de somente um dos cursos

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s)) # Soma
print(max(s)) # Valor Máximo
print(min(s)) # Valor Mínimo
print(len(s)) # Tamanho