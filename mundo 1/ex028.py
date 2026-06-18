from random import randint


aleat = randint(0, 5)
chute = int(input('Tente adivinhar o número que pensei: '))
if chute == aleat:
    print('Você acertou, parabéns!')
else:
    print(f'Você errou, eu pensei em {aleat}')
