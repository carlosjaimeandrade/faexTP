# 4) Solicite ao usuário o nome de um funcionário e a quantidade de peças produzidas nos últimos 5 dias. Calcule a média de produção diária. 
# Apresente o nome do funcionário, a média e a seguinte mensagem:
# Média ≥ 50 peças/dia: “Ótimo desempenho!”
# Média entre 30 e 49 peças/dia: “Desempenho regular.”
# Média < 30 peças/dia: “Desempenho abaixo do esperado.”


# Solicita o nome do funcionário
nome = input("Digite o nome do funcionário: ")

# Quantos dias de produção
qtd_dias = 5

# Lista para armazenar as produções
producoes = []

#quantidade de peça produzida nos 5 dias
qtd_pecas = int(input(f"Digite a quantidade de peças produzidas: "))

# Calcula a média
media = qtd_pecas / qtd_dias

# Exibe o nome e a média formatada
print(f"Funcionário: {nome}")
print(f"Média de produção diária: {media:.2f} peças/dia")

# Verifica e exibe mensagem
if media >= 50:
    print("Ótimo desempenho!")
elif 30 <= media <= 49:
    print("Desempenho regular.")
else:
    print("Desempenho abaixo do esperado.")
