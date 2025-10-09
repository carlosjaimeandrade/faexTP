# Crie um programa em Python que solicite a dois usuários informarem três números cada.

# Os números de cada usuário devem ser armazenados em um array (lista).

# Cada usuário terá sua própria posição dentro de uma estrutura principal, onde serão guardados os três números que escolheu


#_________________________________________
# sem uso do append
num1_user1 = int(input("informe o primeiro numero"))
num2_user1 = int(input("informe o segundo numero"))
num2_user1 = int(input("informe o terceiro numero"))


num1_user2 = int(input("informe o primeiro numero"))
num2_user2 = int(input("informe o segundo numero"))
num3_user2 = int(input("informe o terceiro numero"))

#primeira forma
numeros = [
    [num1_user1, num2_user1, num2_user1],
    [num1_user2, num2_user2, num3_user2]
]
print(numeros)


#_________________________________________
# usando append
lista_user1 = []
num1_user1 = int(input("informe o primeiro numero"))
num2_user1 = int(input("informe o segundo numero"))
num2_user1 = int(input("informe o terceiro numero"))
lista_user1.append(num1_user1)
lista_user1.append(num2_user1)
lista_user1.append(num2_user1)

lista_user2 = []
num1_user2 = int(input("informe o primeiro numero"))
num2_user2 = int(input("informe o segundo numero"))
num3_user2 = int(input("informe o terceiro numero"))
lista_user2.append(num1_user2)
lista_user2.append(num2_user2)
lista_user2.append(num3_user2)

numeros = []
numeros.append(lista_user1)
numeros.append(lista_user2)

print(numeros)