def ficha(jogador='<desconhecido>', gols=0):
    """
    :param jogador: recebe o nome de um jogador, caso não, recebe <desconhecido>
    :param gols: recebe quantidade de gols, caso não recebe 0
    :print: retorna a ficha do jogador, nome e nº de gols
    """
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
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gols=g)
else:
    ficha(j, g)
