# Crie um programa que:
# Solicite ao usuário 10 nomes, um de cada vez.
# A coleta deve ser feita utilizando a estrutura de repetição for.
# Armazene cada nome em uma lista.
# Ao final, percorra a lista utilizando um for e exiba todos os nomes salvos na tela.
	

# #dica use o for junto com range


# Criar lista vazia para armazenar os nomes
nomes = []

# Solicitar 10 nomes usando for com range
for i in range(10):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

# Exibir todos os nomes salvos
print("\n--- LISTA DE NOMES ---")
for nome in nomes:
    print(nome)
