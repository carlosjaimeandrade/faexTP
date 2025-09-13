# Crie um programa que:

# Solicite ao usuário 5 números. 
# Armazene todos os valores em uma lista.
# Após coletar os 5 números, o programa deve calcular e exibir:
# A soma total dos números.
# A média dos números.
# O menor número informado.
# O maior número informado.


# Solicita os 5 números diretamente ao usuário
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
n4 = int(input("Digite o 4º número: "))
n5 = int(input("Digite o 5º número: "))

numeros = []

#adicionando dentro da lista numeros
numeros.append(n1)
numeros.append(n2)
numeros.append(n3)
numeros.append(n4)
numeros.append(n5)

soma_total = sum(numeros) #função sum soma todos os numeros dentro da lista
print(f"Total {soma_total}")
menor_num = min(numeros) #função min pega o menor numero
print(f"Total {menor_num}")
maior_num = max(numeros) #função max pega o menor numero
print(f"Total {maior_num}")

media = soma_total/5 # calculo da media
print(f"media {media}")