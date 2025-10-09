# 1) Crie um programa em Python que solicite ao usuário um número entre 0 e 100. Utilize uma estrutura de 
# repetição para validar a entrada, garantindo que apenas valores dentro desse intervalo sejam aceitos.
# 2) Expanda o programa anterior para solicitar quatro números do usuário, também com validação de 0 a 100. 
# Armazene os números em uma lista e, ao final, exiba a lista completa, a média dos números, o maior e o menor valor informado.
# Amplie o programa do item 2) incluindo uma opção para o usuário escolher entre realizar uma nova entrada de 
# números ou sair do sistema. O programa deve repetir a solicitação de números enquanto o usuário desejar continuar.

continuar = 1
#cria a estrutura de repetição para o menu
while continuar == 1:
    numero1 = float(input('Informe o primeiro numero de 0 até 100: ')) #solictando a entrada de dados para o usuário
    # estrutura de repetição para validar entrada de dados 
    while numero1 > 100:
        numero1 = float(input('Ops o numero deve ser de 0 até 100, tente novamente: '))

    numero2 = float(input('Informe o segundo numero de 0 até 100: ')) #solictando a entrada de dados para o usuário
    # estrutura de repetição para validar entrada de dados 
    while numero2 > 100:
        numero2 = float(input('Ops o numero deve ser de 0 até 100, tente novamente: '))

    numero3 = float(input('Informe o terceiro numero de 0 até 100: ')) #solictando a entrada de dados para o usuário
    # estrutura de repetição para validar entrada de dados 
    while numero3 > 100:
        numero3 = float(input('Ops o numero deve ser de 0 até 100, tente novamente: '))

    numero4 = float(input('Informe o quarto numero de 0 até 100: ')) #solictando a entrada de dados para o usuário
    # estrutura de repetição para validar entrada de dados 
    while numero4 > 100:
        numero4 = float(input('Ops o numero deve ser de 0 até 100, tente novamente: '))

    numeros = [] #criando uma lista para armazenar todos os numeros inserido pelo usuário
    numeros.append(numero1) # função append para adicioanr dentro da lista
    numeros.append(numero2) # função append para adicioanr dentro da lista
    numeros.append(numero3) # função append para adicioanr dentro da lista
    numeros.append(numero4) # função append para adicioanr dentro da lista

    media_numeros = sum(numeros) / 4 # chama função sum para somar todos os index dentro da lista e divide por 4 para obter a media
    menor_numero = min(numeros) # usa a função min para pegar o menor numero da lista
    maior_numero = max(numeros) # usa função max para obter o maior valor da lista

    print('-----------RESULTADO-----------')
    print(f"A lista de numeros é {numeros}")
    print(f"O menor numero da lista é {menor_numero}")
    print(f"O maior numero da lista é {maior_numero}")
    print(f"A media é {media_numeros}")
    print('-------------------------------')

    #apresenta o menu para o usuário
    print('-----------MENU-----------')
    print('1 - Deseja fazer mais um calculo ')
    print('2 - Sair ')
    continuar = int(input()) #solicita o numero do menu, caso seja 1 será solicitado novamente o numeros
