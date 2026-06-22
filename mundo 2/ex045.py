"""Jogo de jokenpo"""


from random import randint
from time import sleep


itens = ['Pedra', 'Papel', 'Tesoura']
# escolha do computador e do jogador
computador = randint(0, 2)
jogador = int(input('Sua jogada: [0 - Pedra][1 - Papel][2 - Tesoura] '))
if jogador not in [0, 1, 2]:
    print('Jogada inválida!')
    quit()
else:
    print('Jo...', end='')
    sleep(1)
    print('Ken...', end='')
    sleep(1)
    print('Pô!')
    sleep(1)
    print('-=' * 30)
    print(f'Você jogou {itens[jogador]}!')
    print(f'O computador jogou {itens[computador]}')
    print('-=' * 30)
    if itens[jogador] == itens[computador]:
        print('Deu empate!')
    elif itens[jogador] == 'Pedra':
        if itens[computador] == 'Papel':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
    elif itens[jogador] == 'Papel':
        if itens[computador] == 'Tesoura':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
    elif itens[jogador] == 'Tesoura':
        if itens[computador] == 'Pedra':
            print('Você perdeu!')
        else:
            print('Você ganhou!')
