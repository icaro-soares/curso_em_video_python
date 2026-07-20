# nome, partidas, qntd gols partida, gols no total
ficha = {}
núm_gols = []
ficha['nome'] = input('Nome do jogador: ').strip()
tot_part = int(input(f'Quantas partidas {ficha['nome']} jogou: '))
for c in range(0, tot_part):
    núm_gols.append(int(input(f'Nº de gols na {c+1}ª partida: ')))
ficha['gols'] = núm_gols[:]
ficha['total_gols'] = sum(núm_gols)
print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
for p in enumerate(núm_gols):
    print(f'Na {p[0]+1}ª partida fez {p[1]} gols.')