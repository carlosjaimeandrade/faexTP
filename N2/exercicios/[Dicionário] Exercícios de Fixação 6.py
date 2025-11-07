# Crie um programa em Python que cadastre informações de 5 pessoas usando lista + dicionários.

# O programa deve:
# Solicitar ao usuário o nome, a idade e a cidade de cada pessoa;
# Armazenar esses dados em um dicionário, com as chaves: "nome", "idade" e "cidade";
# Guardar cada dicionário dentro de uma lista;
# Após todos os cadastros, exibir a lista completa com os dados de todas as pessoas cadastradas.



pessoas = []  # Lista que vai armazenar os dicionários

for i in range(5):  # Loop para cadastrar 5 pessoas
    print(f"\nCadastro da {i + 1}ª pessoa:")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")

    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }

    pessoas.append(pessoa)  # Adiciona o dicionário na lista

# Exibe a lista completa com todos os cadastros
print("\n--- Lista de Pessoas Cadastradas ---")
for p in pessoas:
    print(f"Nome: {p['nome']}, Idade: {p['idade']}, Cidade: {p['cidade']}")

    