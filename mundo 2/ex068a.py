from random import randint


perder = False
vitorias = 0
while not perder:
    itens = ['pedra', 'papel', 'tesoura']
    computador = randint(0, 2)
    jogador = int(input('Escolha [0 - Pedra][1 - Papel][2 - Tesoura] '))
    if jogador not in [0, 1, 2]:
        print('Jogada inválida!')
        quit()
    print('-=' * 30)
    print(f'Escolha do jogador: {itens[jogador]}.\nEscolha do computador: {itens[computador]}.')
    print('-=' * 30)
    if itens[jogador] == itens[computador]:
        print('Deu empate!')
    elif itens[jogador] == 'pedra':
        if itens[computador] == 'papel':
            print('O computador venceu!')
            perder = True
        else:
            print('O jogador venceu!')
            vitorias += 1
    elif itens[jogador] == 'papel':
        if itens[computador] == 'tesoura':
            print('O computador venceu!')
            perder = True
        else:
            print('O jogador venceu!')
            vitorias += 1
    else: # tesoura
        if itens[computador] == 'pedra':
            print('O computador venceu!')
            perder = True
        else:
            print('O jogador venceu!')
            vitorias += 1
print('-=' * 30)
print(f'Ótimo jogo. Total de vitórias: {vitorias}.')
