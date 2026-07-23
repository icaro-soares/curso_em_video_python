def ficha(jogador='<desconhecido>', gols=0):
    print(f'Jogador: {jogador}\nGols: {gols}')


ficha('Romário', 3)
ficha('Pelé')
ficha(gols=10)
ficha()
print('-=' * 30)
print('Sua vez!')
j = input('Nome: ')
g = input('Gols: ')
if g.isnumeric():
    int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
