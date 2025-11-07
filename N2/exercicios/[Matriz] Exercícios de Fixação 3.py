# Crie um sistema de agendamento em que cada usuário possa registrar 4 compromissos.
# Para cada agendamento, o usuário deverá informar nome e data.
# Regras:
# - Não é permitido cadastrar dois agendamentos com a mesma data.
# - Todos os agendamentos devem ser armazenados em uma matriz (lista de listas)
#   no formato: [["Jose", "10/10/2025"], ["Pablo", "10/11/2025"]]

agendamentos = []  # Lista principal (matriz)
datas_usadas = set()  # Conjunto para evitar duplicidade de datas

print("=== Sistema de Agendamento ===")

for i in range(4):  # Cada usuário pode registrar 4 compromissos
    print(f"\nCadastro do {i + 1}º agendamento:")
    nome = input("Digite o nome: ")
    
    while True:
        data = input("Digite a data (ex: 10/10/2025): ")
        if data in datas_usadas:
            print(" Essa data já foi agendada. Escolha outra.")
        else:
            datas_usadas.add(data)
            break

    agendamentos.append([nome, data])

# Exibir todos os agendamentos
print("\n--- Lista de Agendamentos ---")
for ag in agendamentos:
    print(f"Nome: {ag[0]} | Data: {ag[1]}")
