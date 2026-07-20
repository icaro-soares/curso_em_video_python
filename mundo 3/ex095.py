# nome, partidas, qntd gols partida, gols no total, funcionar + de 1
import os


ficha = {}
núm_gols = []
dados = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
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
os.system('cls' if os.name == 'nt' else 'clear')
print('-' * 60)
print(f'{'cód':<7}{'nome'}{'total gols':>25}')
for i, j in enumerate(dados):
    print(f'{i:<7}{j['nome']}{j['total_gols']:>20}')
print('-' * 60)
jog = ' '
while jog != 999:
    jog = int(input('Qual jogador deseja ver o aproveitamento? [999 p/ parar] '))
    if jog in range(len(ficha)):
        print(f'Levantamento de {ficha['nome']}')
        print('-' * 30)
        for d in range(dados):
            print(f'Na partida {d+1} fez {dados[jog]['gols']}')
