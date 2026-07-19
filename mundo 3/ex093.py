ficha = {}
partidas = []
ficha['nome'] = input('Nome do jogador: ').strip().title()
total_partidas = int(input(f'Quantas partidas {ficha['nome']} jogou? '))
for c in range(0, total_partidas):
    partidas.append(int(input(f'Gols na {c+1}ª partida: ')))
ficha['gols'] = partidas[:]
ficha['total_gols'] = sum(ficha['gols'])
print('-=' * 30)
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}.')
print('-=' * 30)
print(f'O jogador {ficha['nome']} jogou {total_partidas} partidas.')
for i, p in enumerate(partidas):
    print(f'\t=> Na {i+1}ª partida, fez {p} gols.')
