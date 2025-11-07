# Crie um sistema que solicite 5 números de 0 até 10.
# Deve ser solicitado os 5 números utilizando o for.
# Deve ser criada a validação usando while.
# Caso o número informado esteja fora da regra, solicite novamente.
# Adicione cada número informado em uma lista.
# Apresente a média, o menor valor e o maior valor.

numeros = []  # Lista para armazenar os números

for i in range(5):  # Loop para solicitar 5 números
    while True:  # Validação com while
        try:
            numero = float(input(f"Digite o {i + 1}º número (entre 0 e 10): "))
            if 0 <= numero <= 10:
                numeros.append(numero)
                break  # Sai do while se o número for válido
            else:
                print(" Número fora do intervalo! Digite um valor entre 0 e 10.")
        except ValueError:
            print("⚠️ Valor inválido! Digite apenas números.")

# Cálculos
media = sum(numeros) / len(numeros)
menor = min(numeros)
maior = max(numeros)

# Exibição dos resultados
print("\n--- RESULTADOS ---")
print(f"Números informados: {numeros}")
print(f"Média: {media:.2f}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
