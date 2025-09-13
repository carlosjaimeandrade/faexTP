while True:  # menu principal
    # Solicita o nome do usuário
    nome = input("Digite o nome do usuário: ")

    # Lista para armazenar os valores das contas
    contas = []

    # Coleta os 6 valores com for
    for i in range(6):
        valor = float(input(f"Digite o valor da conta do {i+1}º mês: "))
        contas.append(valor)

    # Cálculos
    total = sum(contas)
    media = total / 6
    maior = max(contas)
    menor = min(contas)

    # Exibição dos resultados
    print("\n--- RESULTADOS ---")
    print("Usuário:", nome)
    print("Contas informadas:")
    for valor in contas:
        print(f"R$ {valor:.2f}") #usamos o :.2f para travar a casa decimal em 2, mas não é obrigatorio
    print(f"Total gasto: R$ {total:.2f}") #usamos o :.2f para travar a casa decimal em 2, mas não é obrigatorio
    print(f"Média mensal: R$ {media:.2f}") #usamos o :.2f para travar a casa decimal em 2, mas não é obrigatorio
    print(f"Maior valor pago: R$ {maior:.2f}") #usamos o :.2f para travar a casa decimal em 2, mas não é obrigatorio
    print(f"Menor valor pago: R$ {menor:.2f}") #usamos o :.2f para travar a casa decimal em 2, mas não é obrigatorio

    # Menu para repetir ou sair
    opcao = input("\nDeseja executar novamente? (S/N): ").strip().upper()
    if opcao != "S":
        print("Encerrando o programa. Até logo!")
        break
