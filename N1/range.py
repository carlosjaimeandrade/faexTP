# Exemplo 1
numeros = list(range(10))  
print(numeros)  
# Explicação:
# Quando usamos apenas range(10), o Python entende que é de 0 até 9 
# Então o resultado será: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Exemplo 2
numeros = list(range(0, 10))  
print(numeros)  
# Explicação:
# Aqui indicamos explicitamente o início (0) e o fim (10).
# O resultado é o mesmo do anterior: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# Exemplo 3
numeros = list(range(0, 6, 2)) 
print(numeros)  
# Explicação:
# Nesse caso temos três parâmetros: start=0, stop=6, step=2.
# Ou seja: começa em 0, vai até 5 (um antes do 6), pulando de 2 em 2.
# Resultado: [0, 2, 4]