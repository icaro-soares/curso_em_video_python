# nome, partidas, qntd gols partida, gols no total, funcionar + de 1
ficha = {}
núm_gols = []
dados = []
while True:
    núm_gols.clear()
    ficha['nome'] = input('Nome do jogador: ').strip()
    tot_part = int(input(f'Quantas partidas {ficha['nome']} jogou: '))
    for c in range(0, tot_part):
        núm_gols.append(int(input(f'Nº de gols na {c+1}ª partida: ')))
    ficha['gols'] = núm_gols[:]
    ficha['total_gols'] = sum(núm_gols)
    dados.append(ficha.copy())
    resp = ' '
    while resp not in 'SsNn':
        resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break
print('-' * 30)
print(ficha)
print('-' * 30)
print(f'{'cód':<10}{'nome'}{'total gols':>12}')
for i, j in enumerate(dados):
    print(f'{i:<10}{j['nome']}{j['total_gols']:>12}')
print('-' * 30)
jog = ' '
while jog != 999:
    jog = int(input('Qual jogador deseja ver o aproveitamento? [999 p/ parar] '))
    if jog in range(len(dados)):
        print(f'Levantamento de {dados[jog]['nome']}')
        print('-' * 30)
        for d in dados[jog]['gols']:
            print(f'Na partida {d+1} fez {dados[jog]['gols']}')
