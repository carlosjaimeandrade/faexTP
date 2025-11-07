# Crie um programa em Python que cadastre informações de 2 pessoas usando lista + dicionários.

# O programa deve:
# Solicitar ao usuário o seu nome e 5 filmes favoritos;
# Armazenar esses dados em um dicionário, com as chaves: "nome", “filmes“
# A chave filmes deve ser uma lista com os 5 filmes favoritos
# Guardar cada dicionário dentro de uma lista;
# Após todos os cadastros, exibir a lista completa com os dados de todas as pessoas cadastradas.


pessoas = []  # Lista para armazenar os dicionários

for i in range(2):  # Loop para cadastrar 2 pessoas
    print(f"\nCadastro da {i + 1}ª pessoa:")
    nome = input("Digite o nome: ")

    filmes = []  # Lista para armazenar os 5 filmes da pessoa
    for j in range(5):
        filme = input(f"Digite o {j + 1}º filme favorito: ")
        filmes.append(filme)

    pessoa = {
        "nome": nome,
        "filmes": filmes
    }

    pessoas.append(pessoa)  # Adiciona o dicionário à lista principal

# Exibe a lista completa com todos os cadastros
print("\n--- Lista de Pessoas e Seus Filmes Favoritos ---")
for p in pessoas:
    print(f"\nNome: {p['nome']}")
    print("Filmes favoritos:")
    for filme in p["filmes"]:
        print(f" - {filme}")
