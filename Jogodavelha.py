jogovelha = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def Tabela():
    print('                                                            │     │')
    print(
        f'                                                        {jogovelha[0]}   │  {jogovelha[1]}  │   {jogovelha[2]}')
    print(f'                                                     _______│_____│______')
    print('                                                            │     │')
    print(
        f'                                                        {jogovelha[3]}   │  {jogovelha[4]}  │   {jogovelha[5]}')
    print(f'                                                     _______│_____│______')
    print(
        f'                                                        {jogovelha[6]}   │  {jogovelha[7]}  │   {jogovelha[8]}')
    print('                                                            │     │ ')
    print('\n' * 8)


def Verifica_Vitoria(simbolo):
    Tabela()
    if jogovelha[0] == simbolo and jogovelha[3] == simbolo and jogovelha[6] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[1] == simbolo and jogovelha[4] == simbolo and jogovelha[7] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[2] == simbolo and jogovelha[5] == simbolo and jogovelha[8] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[0] == simbolo and jogovelha[1] == simbolo and jogovelha[2] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[3] == simbolo and jogovelha[4] == simbolo and jogovelha[5] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[6] == simbolo and jogovelha[7] == simbolo and jogovelha[8] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[2] == simbolo and jogovelha[4] == simbolo and jogovelha[6] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()
    if jogovelha[0] == simbolo and jogovelha[4] == simbolo and jogovelha[8] == simbolo:
        print(f'Jogador {simbolo} ganhou!')
        exit()


jogador = input('Você quer ser X ou O?').upper()
contador = 0
while True:
    if jogador == 'X':
        while jogador == 'X':
            jogada = int(input(f'Jogada {jogador}: (Apenas de 1 até 9)'))
            if jogada == jogada >= 1 and jogada <= 9:
                if jogovelha[jogada - 1] == ' ':
                    jogovelha[jogada - 1] = 'X'
                    Verifica_Vitoria(jogador)
                    jogador = 'O'
                    contador += 1
                else:
                    Tabela()
                    print('Posição já ocupada')
            else:
                Tabela()
    if contador == 9:
        print('EMPATOU!')
        exit()
    if jogador == 'O':
        while jogador == 'O':
            jogada = int(input(f'Jogada {jogador}: (Apenas de 1 até 9)'))
            if jogada == jogada >= 1 and jogada <= 9:
                if jogovelha[jogada - 1] == ' ':
                    jogovelha[jogada - 1] = 'O'
                    Verifica_Vitoria(jogador)
                    jogador = 'X'
                    contador += 1
                else:
                    Tabela()
                    print('Posição já ocupada')
            else:
                Tabela()
