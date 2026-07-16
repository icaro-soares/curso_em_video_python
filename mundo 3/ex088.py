from random import randint
from time import sleep

jogos_mega_sena = []
while len(jogos_mega_sena) < 6:
    n = randint(0, 60)
    if n not in jogos_mega_sena:
        jogos_mega_sena.append(n)
print('-=' * 30)
jogos_mega_sena.sort()
print(f'Seu jogo: {jogos_mega_sena}')
