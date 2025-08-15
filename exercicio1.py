#1) Solicite ao usuário a largura e o comprimento de um terreno, bem como o valor do metro quadrado (m²) em reais praticado na região. 
# Em seguida, calcule e exiba a área total do terreno e o valor total do terreno. Caso a área seja superior a 60 m², adicione R$ 10,00 
# ao valor do metro quadrado antes de calcular o valor total.
#Fórmula:
#Área (m²) = Largura (m) × Comprimento (m)


# Solicita a largura e o comprimento do terreno
largura = float(input("Informe a largura do terreno (em metros): "))
comprimento = float(input("Informe o comprimento do terreno (em metros): "))

# Calcula a área do terreno
area = largura * comprimento
print(f"A área do terreno é {area:.2f} m².")

# Solicita o valor do metro quadrado
valor_m2 = float(input("Informe o valor do m² em reais praticado na região: R$ "))

# Verifica se há adicional
if area > 60:
    valor_m2 += 10  # Acrescenta R$ 10,00 por m²

# Calcula o valor total do terreno
valor_total = area * valor_m2
print(f"O valor total do terreno é R$ {valor_total:.2f}.")