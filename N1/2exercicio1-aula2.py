# 1) Solicite ao usuário seu nome e as notas correspondentes às quatro fases do projeto, 
# garantindo que cada nota esteja dentro do limite máximo permitido (10, 20, 25 e 45 pontos, respectivamente).
# Em seguida, calcule a nota final somando as quatro entregas e exiba o nome do aluno, a nota final e a situação, 
# indicando “Aprovado” para notas finais maiores ou iguais a 60 e “Reprovado” para notas abaixo de 60. Certifique-se de validar
# as entradas, impedindo que sejam informados valores superiores ao teto de cada entrega, tornando o processo de cálculo mais confiável e seguro.



# Solicita o nome do aluno
nome = input("Digite o nome do aluno: ")

# Solicita a nota da 1ª entrega (máximo 10 pontos) e valida
nota1 = float(input("Digite a nota da 1ª entrega (0 a 10): "))
while nota1 > 10:
    print("Nota inválida! Deve ser entre 0 e 10.")
    nota1 = float(input("Digite a nota da 1ª entrega (0 a 10): "))

# Solicita a nota da 2ª entrega (máximo 20 pontos) e valida
nota2 = float(input("Digite a nota da 2ª entrega (0 a 20): "))
while nota2 > 20:
    print("Nota inválida! Deve ser entre 0 e 20.")
    nota2 = float(input("Digite a nota da 2ª entrega (0 a 20): "))

# Solicita a nota da 3ª entrega (máximo 25 pontos) e valida
nota3 = float(input("Digite a nota da 3ª entrega (0 a 25): "))
while nota3 > 25:
    print("Nota inválida! Deve ser entre 0 e 25.")
    nota3 = float(input("Digite a nota da 3ª entrega (0 a 25): "))

# Solicita a nota da 4ª entrega (máximo 45 pontos) e valida
nota4 = float(input("Digite a nota da 4ª entrega (0 a 45): "))
while nota4 > 45:
    print("Nota inválida! Deve ser entre 0 e 45.")
    nota4 = float(input("Digite a nota da 4ª entrega (0 a 45): "))

# Calcula a nota final somando todas as entregas
nota_final = nota1 + nota2 + nota3 + nota4

# Determina a situação do aluno
if nota_final >= 60:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Exibe o resultado final
print("\nAluno:", nome)
print("Nota final:", nota_final)
print("Situação:", situacao)
