#Exercícios de revisão 2
# Crie um programa que:

# Solicite ao usuário que informe seu nome e sua idade.
# Verifique se a idade informada é maior que 20 anos.

# Exiba na tela uma mensagem final que concatene o nome e a idade do usuário, junto com a informação do resultado da verificação.


# Solicita ao usuário que informe seu nome
nome = input("Digite seu nome: ")

# Solicita ao usuário que informe sua idade
# A função input() retorna uma string, então convertemos para inteiro com int()
idade = int(input("Digite sua idade: "))

# Verifica se a idade é maior que 20
if idade > 20:  
    # Exibe a mensagem final concatenando nome, idade e o resultado da verificação
    print(f"Idade maior que 20, nome: {nome} idade: {idade}")
