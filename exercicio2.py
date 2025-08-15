# Solicite ao usuário o seu nome e suas respectivas notas nas 4 fases do projeto.  Calcule a nota final do aluno
# (1ª entrega 10ptos, 2ª entrega 20ptos, 3ª entrega 25 pontos e 4ª entrega 45 ptos). Apresente o nome do aluno,
# a sua nota final (a soma das quatro entregas) e sua situação final sendo Aprovado para nota final >= 60 e Reprovado para nota final <60.

# Solicita ao usuário que digite seu nome e armazena na variável 'nome'
nome = input("Digite o nome do aluno: ")

# Solicita a nota da 1ª entrega (peso 10 pontos)
nota1 = float(input("Digite a nota da 1ª entrega (0 a 10): "))

# Solicita a nota da 2ª entrega (peso 20 pontos)
nota2 = float(input("Digite a nota da 2ª entrega (0 a 20): "))

# Solicita a nota da 3ª entrega (peso 25 pontos)
nota3 = float(input("Digite a nota da 3ª entrega (0 a 25): "))

# Solicita a nota da 4ª entrega (peso 45 pontos)
nota4 = float(input("Digite a nota da 4ª entrega (0 a 45): "))

# Calcula a nota final somando todas as notas
nota_final = nota1 + nota2 + nota3 + nota4

# Verifica se a nota final é maior ou igual a 60 para aprovação
if nota_final >= 60:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

# Exibe o nome do aluno
print("Aluno:", nome)

# Exibe a nota final
print("Nota final:", nota_final)

# Exibe a situação final
print("Situação:", situacao)
