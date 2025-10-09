# Programa que solicita 5 números ao usuário,
# armazena em uma lista e exibe todos no final.

# Criando uma lista vazia para guardar os números
numeros = []

# Laço for que vai rodar 5 vezes (0 até 4)
for i in range(5):
    # Solicita ao usuário digitar um número
    numero = int(input(f"Digite o {i+1}º número: "))
    
    # Adiciona o número na lista
    numeros.append(numero)

# Exibe todos os números armazenados na lista
print("\nOs números digitados foram:")
for n in numeros:
    print(n)
