# Solicite ao usuário o nome de um funcionário e a quantidade de peças produzidas nos últimos 5 dias. Calcule a média de produção diária. 
# Apresente o nome do funcionário, a média e a seguinte mensagem:
# Média ≥ 50 peças/dia: “Ótimo desempenho!”
# Média entre 30 e 49 peças/dia: “Desempenho regular.”
# Média < 30 peças/dia: “Desempenho abaixo do esperado.”

# Solicita o nome do funcionário
nome = input("Digite o nome do funcionário: ")

# Solicita a produção dos últimos 5 dias
dia1 = int(input("Digite a quantidade de peças produzidas no 1º dia: "))
dia2 = int(input("Digite a quantidade de peças produzidas no 2º dia: "))
dia3 = int(input("Digite a quantidade de peças produzidas no 3º dia: "))
dia4 = int(input("Digite a quantidade de peças produzidas no 4º dia: "))
dia5 = int(input("Digite a quantidade de peças produzidas no 5º dia: "))

# Calcula a média
media = (dia1 + dia2 + dia3 + dia4 + dia5) / 5

# Exibe resultados
print("\n--- RESULTADO ---")
print("Funcionário:", nome)
print("Média de produção diária:", media)

# Verifica desempenho
if media >= 50:
    print("Ótimo desempenho!")
elif 30 <= media <= 49:
    print("Desempenho regular.")
else:
    print("Desempenho abaixo do esperado.")
