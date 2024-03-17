"""
Estudo de caso de listas em python

# Podemos facilmenter chegar se determinado valor está contido na lista
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

# adicionar elementos em listas

Para adicionar elementos em listas, utilizamos a função append
Com append, nós só conseguimos adicionar um elemento por vez.

print(lista1)
lista1.append(49)
print(lista1)

# coloca uma lista dentro da lista, criando assim um vetor (elemento único, porém ele é uma lista)
print(lista1)
lista1.append([49, 5])
print(lista1)

# adiciona mais itens na lista existente porém não aceita valor único.
lista1.extend([134, 44, 67])
print(lista1)

# podemos inserir um novo elemento na lista informando a posição do índice
# isso não substitui o valor inicial, o mesmo será deslocado para a direita
lista1.insert(4, 'Novo Valor')
print(lista1)

#lista1 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# forma1: podemos facilmente inverter uma lista
lista1.reverse()
lista2.reverse()

# forma 2: usando o slice
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# contar os elementos de uma lista
print(len(lista1))

# removendo elementos de uma lista

print(lista5)
lista5.pop()
print(lista5)

# removendo elemento pelo índice
lista5.pop(2)
print(lista5)

# zerar a lista
print(lista5)
lista5.clear()
print(lista5)

# podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3, 4]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca % entre cada elemento e transforma em uma string
curso = '%'.join(lista6)
print(curso)


# iterando sobre listas

# exemplo 1
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
    print(soma)

# exemplo 2

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5, 6]
print(numeros)

# fazemos acessos aos elementos de forma indexada

cores = ['verde', 'amarelo', 'rosa', 'vermelho']
print(cores[0])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
cores = ['verde', 'amarelo', 'rosa', 'vermelho']
print(cores[-2])

for cor in cores:
    print(cor)

index = 0
while index < len(cores):
    print(cores[index])
    index = index + 1

gerar index no for com o enumerate
for index, cor in enumerate(cores):
    print(index, cor)

#listas aceitam repetições em python


# Encontrar indice de um elemento na lista
# Ele retorna o índice do primeiro elemento encontrado

numeros = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
print(numeros.index(44))

# em qual indice está o valor 4
print(numeros.index(27))

# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar
# buscando a partir do indice 1
print(numeros.index(22, 1))
print(numeros.index(22, 2))
#OBS: caso não tenha este elemento na lista, será apresentado ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(22, 1, 8))

# Revisão slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# trabalhando com slice de lista com o parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[1:])

# trabalhando com slice de lista com o parametro 'fim'
print(lista[:2]) # começa em 0 e pega até o índice 2 - 1

print(lista[:4]) # começa em 0 e pega até o índice 4 - 1

print(lista[1:3]) # começa em 1, pega até o índice 3 - 1


# trabalhando com slice de lista com o parâmetro 'passo'
print(lista[1::2]) # começa em 1, vai até o final, de 2 em 2

print(lista[::2]) # começa em 0, vai até o final, de 2 em 2


#invertendo valores em uma lista
nomes = ['Geek', 'University']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)


# Soma*, Valor Max*, Valor Min*, Tamanho
# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
# Se tivermos mais elementos para desempacotar do que variáveis para receber os valores, teremos ValeuError
lista = [1, 2, 3, 4, 5, 6]

num1, num2, num3, num4, num5, num6 = lista
print(num1)
print(num2)
print(num3)
print(num4)
print(num5)
print(num6)

# Forma 1 Deep Copy (Copiando Lista)

print(lista1)
nova = lista1.copy()
print(nova)
nova.append(4)

print(lista1)
print(nova)


"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', '', 'U']
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')


# Forma 2 Shallow Copy - Utilizamos a cópia via atribuição, contudo após realizar modificação em uma, altera na outra.
# Isso em python é chamado de shallow copy

print(lista1)
nova = lista1
print(nova)
nova.append(4)
print(lista1)
print(nova)