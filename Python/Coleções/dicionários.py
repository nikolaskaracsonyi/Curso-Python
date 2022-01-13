"""
Dicionários

OBS: Em algumas linguagens de programação os dicionários Python são conhecidos 
por mapas.

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves "{}".

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos: "chave: valor";
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}

print(paises)
print(type(paises))


# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
# print(paises['ru'])  Caso haja a tentativa de acessar uma chave que não existe, teremos o erro "KeyError"

# Forma 2 - Acessando via get (Recomendada)

print(paises.get('br'))
print(paises.get('ru'))

pais = paises.get('ru')


# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado o erro "KeyError".

if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


# Podemos definir um valor padrão caso não encontremos o objeto com a chave informada

pais = paises.get('py', 'Não encontrado')

print(f'Encontrei o país {pais}')


# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive listas, tuplas e dicionários como chaves
# de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionários, pois as mesmas
# são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova Iorque',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))


# Adicionar elementos em um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 (Mais comum)

receita['abr'] = 350

print(receita)

# Forma 2

novo_dado = {'mai': 500}

receita.update(novo_dado) # receita.update({'mai': 500})

print(receita)

# Atualizando dados em um dicionário

# Forma 1

receita['mai'] = 550

print(receita)

# Forma 2

receita.update({'mai': 600})

print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# Conclusão 2: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário

receita = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 (Mais comum)

ret = receita.pop('mar')

print(ret)

print(receita)

# OBS 1: Para utilizar o pop em dicionários é necessário SEMPRE informar a chave, e caso não encontre o elemento um "KeyError" é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev']

print(receita)

# OBS 1: Se a chave não existir será gerado um "KeyError".
# OBS 2: Nesse caso o valor removido não é retornado.
"""

# Imagine que você tem um E-commerce onde temos um carrinho de compras no qual adicionamos produtos

"""
Carrinho de Compras:
    Produto 1:
        - nome;
        - quantidade;
        - preço;
    Produto 2:
        - nome;
        - quantidade;
        - preço;

"""

# Forma 1 - Poderiamos utilizar uma Lista

carrinho = []

produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual o índice de cada informação para cada produto.

# Forma 2 - Poderiamos utilizar uma Tupla

produto1 = ('Plastation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual o índice de cada informação para cada produto.

# Forma 3 - Poderiamos utilizar um Dicionário

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
