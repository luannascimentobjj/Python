"""
Recebendo dados do usuário.
"""
# entrada de dados
print("Qual seu nome?")
nome = input()

# Exemplo de print antigo
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo print 3.7>
print(f'Seja bem vindo(a) {nome}')

# print('Qual a sua idade?')
# idade = input()

idade = int(input('Qual a sua idade? '))

# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print moderno 3.x
# print('A {0} tem {1} anos' .format(nome, idade))

print(f'O {nome} tem {idade} anos')
print(f'O {nome} nasceu em {2024 - idade}')