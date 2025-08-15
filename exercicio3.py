# Solicite ao usuário o valor da total das despesas do mês e das entradas do mês. Em seguida, retorne o saldo final do usuário e apresente as mensagens:
# Se saldo > 0  - “Parabéns! Está no Positivo!”
# Se saldo < 0 – “Perigo! Está no Vermelho!”
# Se saldo = 0 – “Alerta! Está no limite!”

# Solicita ao usuário o valor total das despesas do mês
despesas = float(input("Digite o valor total das despesas do mês: "))

# Solicita ao usuário o valor total das entradas (receitas) do mês
entradas = float(input("Digite o valor total das entradas do mês: "))

# Calcula o saldo final (entradas - despesas)
saldo = entradas - despesas

# Exibe o saldo final para o usuário, :.2f é para colocar apenas 2 casas decimais
print(f"Seu saldo final é: R$ {saldo:.2f}")

# Verifica se o saldo é positivo
if saldo > 0:
    # Mensagem para saldo positivo
    print("Parabéns! Está no Positivo!")
# Verifica se o saldo é negativo
elif saldo < 0:
    # Mensagem para saldo negativo
    print("Perigo! Está no Vermelho!")
# Caso não seja positivo nem negativo, é zero
else:
    # Mensagem para saldo igual a zero
    print("Alerta! Está no limite!")
