# O bloco try/except serve para tratar possíveis erros que podem ocorrer
# durante a execução do código — especialmente erros causados por entradas inválidas do usuário.
# 
# No exemplo abaixo, o programa tenta converter a entrada do usuário para um número (float).
# Caso o usuário digite algo que não possa ser convertido (como letras ou símbolos),
# o Python gera um erro (ValueError) e o fluxo do programa é desviado para o bloco "except",
# evitando que o programa pare de funcionar de forma inesperada.
# 
# Assim, garantimos que o sistema continue funcionando e exibimos uma mensagem amigável ao usuário.

try:
    num = float(input('Informe um número: '))
except Exception as e:
    print('Não é permitido digitar letras, apenas números.')
