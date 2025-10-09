# Crie um programa em Python que solicite ao usuário a quantidade de um produto em estoque (entre 0 e 500). 
# Utilize uma estrutura de repetição para validar a entrada, garantindo que apenas valores dentro desse intervalo sejam aceitos.
# Expanda o programa para solicitar a quantidade em estoque de cinco produtos diferentes (valores entre 0 e 500).
#  Armazene os valores em uma lista e, ao final, exiba:
# A lista completa de estoques
# A média de itens em estoque
# O produto com maior quantidade em estoque
# O produto com menor quantidade em estoque
# Amplie o programa do item 2, incluindo uma opção para o usuário escolher entre registrar
#  novos estoques ou sair do sistema. O programa deve repetir a solicitação de quantidades enquanto o usuário desejar continuar


while True:  # Loop principal para repetir o programa enquanto o usuário quiser
    estoques = []  # Lista para armazenar as quantidades de cada produto

    # Loop para solicitar a quantidade de 5 produtos
    for i in range(5):
        while True:  # Loop para validar a entrada do usuário
            try:
                # Solicita ao usuário a quantidade em estoque
                quantidade = int(input(f"Digite a quantidade em estoque do produto {i+1} (0 a 500): "))
                # Verifica se a quantidade está dentro do intervalo permitido
                if 0 <= quantidade <= 500:
                    estoques.append(quantidade)  # Adiciona a quantidade à lista
                    break  # Sai do loop de validação
                else:
                    print("Quantidade inválida! Digite um valor entre 0 e 500.")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")

    # Exibe a lista completa de estoques
    print("\nLista de estoques:", estoques)

    # Calcula e exibe a média de itens em estoque
    media = sum(estoques) / len(estoques)
    print("Média de itens em estoque:", round(media, 2))  # Arredonda para 2 casas decimais

    # Exibe o produto com maior quantidade em estoque
    print("Maior quantidade em estoque:", max(estoques))

    # Exibe o produto com menor quantidade em estoque
    print("Menor quantidade em estoque:", min(estoques))

    # Pergunta ao usuário se deseja registrar novos estoques ou sair
    escolha = input("\nDeseja registrar novos estoques? (s/n): ").lower()
    if escolha != 's':  # Se o usuário não digitar 's', sai do programa
        print("Saindo do sistema...")
        break  # Encerra o loop principal
