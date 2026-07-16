from random import randint
from time import sleep

jogos_mega_sena = []
temp = []
qnt = int(input('Quantos jogos devo criar? '))
for cont in range(0, qnt):
    while len(temp) < 6:
        n = randint(0, 60)
        if n not in jogos_mega_sena:
            temp.append(n)
    jogos_mega_sena.append(temp[:])
    temp.clear()
    cont += 1
print('-=' * 30)
for i, jogo in enumerate(jogos_mega_sena):
    sleep(1)
    print(f'JOGO {i+1}: {sorted(jogo)}')
