
nome = input("informe o nome ")
sala = input("informe a sala ")
quantidade = int(input("informe a quantidade "))

while quantidade <= 0 or quantidade > 10:
    quantidade = int(input("informe a quantidade correta de 1 até 10 "))


if quantidade >= 5:
    preco_unitario = 5
else:
    preco_unitario = 10

preco_final = preco_unitario * quantidade

print(nome)
print(sala)
print(quantidade)
print(preco_unitario)
print(preco_final)


dados_cinemas = []

dados_cinemas.append(nome)
dados_cinemas.append(sala)
dados_cinemas.append(quantidade)
dados_cinemas.append(preco_unitario)
dados_cinemas.append(preco_final)