jogovelha = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def jogo():
    global jogovelha
    print('                                                            │     │')
    print(f'                                                        {jogovelha[0]}   │  {jogovelha[1]}  │   {jogovelha[2]}')
    print(f'                                                     _______│_____│______')
    print('                                                            │     │')
    print(f'                                                        {jogovelha[3]}   │  {jogovelha[4]}  │   {jogovelha[5]}')
    print(f'                                                     _______│_____│______')
    print(f'                                                        {jogovelha[6]}   │  {jogovelha[7]}  │   {jogovelha[8]}')
    print('                                                            │     │ ')
    print('\n'*8)


def vitoria():
    if jogovelha[0] == 'X' and jogovelha[3] == 'X' and jogovelha[6] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[1] == 'X' and jogovelha[4] == 'X' and jogovelha[7] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[2] == 'X' and jogovelha[5] == 'X' and jogovelha[8] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[0] == 'X' and jogovelha[1] == 'X' and jogovelha[2] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[3] == 'X' and jogovelha[4] == 'X' and jogovelha[5] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[6] == 'X' and jogovelha[7] == 'X' and jogovelha[8] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[2] == 'X' and jogovelha[4] == 'X' and jogovelha[6] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[0] == 'X' and jogovelha[4] == 'X' and jogovelha[8] == 'X':
        print('Jogador X ganhou!')
        exit()
    if jogovelha[0] == 'O' and jogovelha[3] == 'O' and jogovelha[6] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[1] == 'O' and jogovelha[4] == 'O' and jogovelha[7] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[2] == 'O' and jogovelha[5] == 'O' and jogovelha[8] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[0] == 'O' and jogovelha[1] == 'O' and jogovelha[2] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[3] == 'O' and jogovelha[4] == 'O' and jogovelha[5] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[6] == 'O' and jogovelha[7] == 'O' and jogovelha[8] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[2] == 'O' and jogovelha[4] == 'O' and jogovelha[6] == 'O':
        print('Jogador O ganhou!')
        exit()
    if jogovelha[0] == 'O' and jogovelha[4] == 'O' and jogovelha[8] == 'O':
        print('Jogador O ganhou!')
        exit()


jogo()
contador = 0
while True:
    while True:
        while True:
            escolha = int(input('Jogada X: '))
            if escolha == escolha >= 1 and escolha <= 9:
                break
            else:
                print('Apenas casa de 1 até 9')
        if jogovelha[escolha - 1] == ' ':
            contador += 1
            jogovelha[escolha - 1] = 'X'
            jogo()
            vitoria()
            break
        else:
            print('Essa casa já está selecionada')
    if contador == 9:
        print('EMPATOU')
        break
    while True:
        while True:
            escolha = int(input('Jogada O: '))
            if escolha == escolha >= 1 and escolha <= 9:
                break
            else:
                print('Apenas casa de 1 até 9')
        if jogovelha[escolha - 1] == ' ':
            contador += 1
            jogovelha[escolha - 1] = 'O'
            jogo()
            vitoria()
            break
        else:
            print('Essa casa já está selecionada')
