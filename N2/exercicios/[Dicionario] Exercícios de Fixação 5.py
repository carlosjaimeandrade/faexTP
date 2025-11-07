# Crie um programa que solicite o nome e a idade de duas pessoas 
# usando o for.Os dados de cada pessoa devem ser armazenados em um dicionário, 
# e ambos os dicionários devem ser guardados dentro de uma lista.


# Crie um programa que solicite o nome e a idade de duas pessoas usando o for.
# Os dados de cada pessoa devem ser armazenados em um dicionário,
# e ambos os dicionários devem ser guardados dentro de uma lista.

pessoas = []  # lista para armazenar os dicionários

for i in range(2):  # repete 2 vezes (para duas pessoas)
    nome = input(f"Digite o nome da {i + 1}ª pessoa: ")
    idade = int(input(f"Digite a idade da {i + 1}ª pessoa: "))
    
    pessoa = {
        "nome": nome,
        "idade": idade
    }
    
    pessoas.append(pessoa)  # adiciona o dicionário à lista

print("\nLista de pessoas cadastradas:")
for p in pessoas:
    print(f"Nome: {p['nome']}, Idade: {p['idade']}")
