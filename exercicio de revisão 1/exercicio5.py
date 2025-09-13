# Crie um programa que:
# Solicite ao usuário dois números.
# Valide cada entrada:
# O número deve ser maior que 0.
# Caso o usuário informe um valor inválido (≤ 0), o programa deve solicitar novamente até que um valor válido seja inserido.
# Após receber os dois números válidos, exiba na tela uma mensagem apresentando a soma dos dois valores.
# Crie um menu perguntando para o usuário se ele deseja realizar a soma de 2 números novamente


# #dica use o while para validar
# # use o while para criar o menu


while True:  # menu principal
    # Solicita e valida o primeiro número
    num1 = int(input("Digite o primeiro número (maior que 0): "))
    while num1 <= 0:
        num1 = int(input("Digite o primeiro número (maior que 0): "))
        if num1 <= 0:
            print("Valor inválido! Tente novamente.")

    # Solicita e valida o segundo número
    num2 = int(input("Digite o segundo número (maior que 0): "))
    while num2 <= 0:
        num2 = int(input("Digite o segundo número (maior que 0): "))
        if num2 <= 0:
            print("Valor inválido! Tente novamente.")

    # Calcula e mostra a soma
    soma = num1 + num2
    print(f"A soma de {num1} + {num2} é = {soma}")

    # Menu para repetir ou sair
    opcao = input("\nDeseja realizar outra soma? (S/N): ").strip().upper()
    if opcao != "S":
        print("Encerrando o programa. Até logo!")
        break
