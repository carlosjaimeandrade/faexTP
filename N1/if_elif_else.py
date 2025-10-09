# Solicitar a pontuação do funcionário
pontuacao = float(input("Digite a pontuação do funcionário: "))

# Verificar desempenho usando if, elif e else
if pontuacao >= 90:
    print("Desempenho: Excelente")
elif pontuacao >= 75:
    print("Desempenho: Bom")
elif pontuacao >= 60:
    print("Desempenho: Regular")
else:
    print("Desempenho: Insatisfatório")
