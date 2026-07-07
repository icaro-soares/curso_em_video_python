lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite o {c+1}º valor: ')))
print('-=' * 30)
print('Sua lista de números: ', end='')
for n in lista:
    print(n, end=' ')
