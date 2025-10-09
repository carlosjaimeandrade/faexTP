# Solicita ao usuário que digite 4 nomes e armazena cada um em uma variável
nome1 = input("Digite o 1º nome: ")
nome2 = input("Digite o 2º nome: ")
nome3 = input("Digite o 3º nome: ")
nome4 = input("Digite o 4º nome: ")

# Cria uma lista contendo todos os nomes coletados
nomes = [nome1, nome2, nome3, nome4]

# Exibe uma mensagem indicando o início da listagem
print("Nomes armazenados:")

# Utiliza um laço for para percorrer a lista 'nomes'
for nome in nomes:
    # Em cada iteração, imprime o nome atual da lista
    print(nome)
