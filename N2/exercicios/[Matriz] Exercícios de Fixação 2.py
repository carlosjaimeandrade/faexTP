# Crie um sistema em que 4 usuários informem valores numéricos.
# Os valores devem ser solicitados utilizando a estrutura for com range.

# Para cada usuário, o sistema deve armazenar os dados em uma matriz                             (lista de listas) no seguinte formato:
# [["José", 10], ["Pablo", 20], ... ]

# Ao final, utilize outro for para somar todos os valores numéricos armazenados na matriz e exibir o resultado da soma.


matriz = []  # Lista principal (matriz)

# Cadastro dos 4 usuários
for i in range(4):
    print(f"\nCadastro do {i + 1}º usuário:")
    nome = input("Digite o nome: ")
    
    while True:  # Validação para garantir que o valor é numérico
        try:
            valor = float(input("Digite um valor numérico: "))
            break
        except ValueError:
            print("Valor inválido! Digite apenas números.")
    
    matriz.append([nome, valor])

# Soma de todos os valores
soma = 0
for item in matriz:
    soma += item[1]

# Exibição dos resultados
print("\n--- DADOS CADASTRADOS ---")
for item in matriz:
    print(f"Nome: {item[0]}, Valor: {item[1]}")

print(f"\n🔹 Soma total dos valores: {soma}")
