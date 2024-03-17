"""
Tipo Float
Casas decimais
OBS: O separadores de casas decimais na programação é ponto
"""

# Errado
valor = 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribução

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para int

res = int(valor)
print(res)
print(type(res))


# Podemos trabalhar com números complexos
variav = 5j