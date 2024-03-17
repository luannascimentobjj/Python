"""
Loop  -> Estrutura de repetição.
For -> Uma das estruturas

nome = 'Luan Nascimento Oliveira'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 200)

# iterando string
for letra in nome:
    print(letra)

# iterando lista
for numero in lista:
    print(numero)

# exemplo for 3 (iterando sobre um range), vali de 1 a 9.
for numero in range(1, 10):
    print(numero)

Usando índice
for i, letra in enumerate(nome):
    print(nome[i])

descartando o índice
    for _, letra in enumerate(nome):
    print(letra)

nome = 'Luan Nascimento Oliveira'
lista = [1, 2, 3, 4, 5, 6]
numeros = range(1, 200)

for _, letra in enumerate(nome):
    print(letra)

qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o  {n}/{qtd} valor: '))
    soma = soma + num
    print(f'A soma é {soma}')

"""

nome = 'Geek University'
for letra in nome:
    print(letra, end='')