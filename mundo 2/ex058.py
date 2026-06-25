from random import randint


computador = randint(0, 10)
chances = 0
print('Pensei em um número, tente adivinhá-lo.')
while True:
    chute = int(input('Seu palpite: '))
    chances += 1
    if chute != computador:
        print('Você errou, tente novamente.', end=' ')
        if chute > computador:
            print('Menos.')
        else:
            print('Mais.')
    else:
        print(f'Parabéns, você acertou!\nTotal de tentativas: {chances}.')
        break
