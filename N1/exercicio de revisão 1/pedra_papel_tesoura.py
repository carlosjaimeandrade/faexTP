pedra_ganha = ['pedra', 'tesoura']
tesoura_ganha = ['tesoura', 'papel']
papel_ganha = ['papel', 'pedra']


usuario_1 = input('Player 1 Faça sua escolha? ')

usuario_2 = input('Player 2 Faça sua escolha? ')

if usuario_1 != usuario_2:
    if usuario_1 in pedra_ganha and usuario_2 in pedra_ganha:
        if (usuario_1 == 'pedra'):
            print('Usuario 1 ganhou: Pedra')
        else:
            print('Usuario 2 ganhou: Pedra')

    if usuario_1 in tesoura_ganha and usuario_2 in tesoura_ganha:
        if (usuario_1 == 'tesoura'):
            print('Usuario 1 ganhou: Pedra')
        else:
            print('Usuario 2 ganhou: Pedra')

    if usuario_1 in papel_ganha and usuario_2 in papel_ganha:
        if (usuario_1 == 'papel'):
            print('Usuario 1 ganhou: Pedra')
        else:
            print('Usuario 2 ganhou: Pedra')
else:
    print('Deu empate')