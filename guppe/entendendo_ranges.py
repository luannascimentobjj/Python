"""

- Precisamos conhecer o loop for para usar os ranges
- Precisamos conhecer o range para trabalhar melhor o loop for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória mas sim de maneira especificada.

Formas gerais:
range(valor_de_parada)
Obs: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# FORMA 1
for num in range(11):
    print(num)


# FORMA 2: Valor de início, valor de parada
for num in range(1, 11):
    print(num)

# FORMA 3: Valor de início, valor de parada, passo especificado pelo usuário
for num in range(1, 11, 2):
    print(num)

"""

# FORMA 4: Valor de final, valor de parada, passo especificado pelo usuário (inversa)
for num in range(10, -1, -2):
    print(num)
