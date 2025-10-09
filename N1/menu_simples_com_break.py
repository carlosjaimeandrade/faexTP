# Loop infinito: o programa vai rodar até que apareça um break
while True:
    # Exibe o menu de opções para o usuário
    print("\n===== MENU DE OPÇÕES =====")
    print("1 - Somar dois números")
    print("2 - Sair")

    # Pede para o usuário escolher uma opção e armazena na variável 'opcao'
    opcao = input("Escolha uma opção: ")

    # Verifica se a opção escolhida foi "1"
    if opcao == "1":
        # Pede o primeiro número e converte para float (aceita inteiros e decimais)
        n1 = float(input("Digite o primeiro número: "))
        # Pede o segundo número
        n2 = float(input("Digite o segundo número: "))
        # Faz a soma dos dois números
        soma = n1 + n2
        # Exibe o resultado da soma usando f-string
        print(f"A soma de {n1} + {n2} = {soma}")

    # Se a opção escolhida for "2", o usuário quer sair
    elif opcao == "2":
        print("Saindo do programa... Até mais!")
        # Interrompe o while True e encerra o programa
        break

    # Caso o usuário digite qualquer valor diferente de "1" ou "2"
    else:
        print("Opção inválida, tente novamente!")
