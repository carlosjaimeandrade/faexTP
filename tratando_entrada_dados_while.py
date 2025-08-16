# Pede para o usuário digitar um número e converte a entrada para float
# Assim, aceita números decimais também
numero = float(input('Informe um numero de 0 a 5: '))

# Enquanto o número for maior que 5, repete o loop
while (numero > 5):
    # Mostra uma mensagem informando que o número está fora do limite
    print('O numero deve ser de 0 até 5')
    # Solicita novamente que o usuário digite um número
    numero = float(input('Informe um numero de 0 a 5: '))

# Quando sair do while, significa que o número está dentro do limite (0 a 5)
# Exibe o número escolhido pelo usuário
print(f"Seu numero é {numero}")
