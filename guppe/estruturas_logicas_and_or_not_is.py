"""
Estruturas Lógicas: and, or, is

Operadores unários:
 -not
 Operadores binários:
 -and, or, is

"""
ativo = True
logado = True

if ativo and logado:
    print('Bem vindo usuário!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')


ativo2 = False
logado2 = True

if not ativo2:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail!')
else:
    print('Bem vindo usuário!')

print(ativo2 is True)
