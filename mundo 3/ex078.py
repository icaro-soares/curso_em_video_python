lista = []
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c+1}: ')))
print('-=' * 30)
print('Sua lista de números: ', end='')
for n in lista:
    print(n, end=' ')
print(f'\nO maior valor é {max(lista)}\nE o menor valor é {min(lista)}.')
print(f'Suas posições são respectivamente: {lista.index(max(lista))+1} e {lista.index(min(lista))+1}')
