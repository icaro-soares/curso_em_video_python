ficha = {}
ficha_temp = {}
partidas = []
while True:
    ficha_temp['nome'] = input('Nome: ')
    tot_part = int(input('Total de partidas: '))
    for c in range(0, tot_part):
        partidas.append(int(input(f'Qnt de gols na {c+1}ª partida: ')))
    ficha_temp['gols'] = partidas[:]
    ficha_temp['tot_gols'] = sum(ficha_temp['gols'])
    partidas.append(ficha_temp.copy())
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ')
    if r in 'Nn':
        break
print('-=' * 30)
print(ficha)
