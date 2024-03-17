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

"""
type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', '', 'U' ]
lista3 = []
lista4 = list(range(11))
lista5 = list('Geek University')

#podemos facilmente inverter uma lista
#lista1.reverse()
#lista2.reverse()

print(lista1[::-1])
print(lista2[::-1])