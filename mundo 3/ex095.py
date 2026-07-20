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
print(f'{'cód':<4}{'nome':<15}{'total gols':<10}')
for i, j in enumerate(dados):
    print(f'{i:<4}{j['nome']:<15}{j['total_gols']:<10}')
print('-' * 60)
jog = ' '
while True:
    jog = int(input('Qual jogador deseja ver o aproveitamento? [999 p/ parar] '))
    if jog == 999:
        print('Volte sempre!')
        break
    if jog >= 0 and jog < len(dados):
        print(f'Levantamento de {dados[jog]['nome']}:')
        for i, gols in enumerate(dados[jog]['gols']):
            print(f'Na partida {i+1} fez {gols} gols.')
        print('-' * 30)
    else:
        print(f'Erro! Não existe jogador com código {jog}!')
