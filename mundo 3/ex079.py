lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    else:
        print('O valor já está na lista.')
    resp = ' '
    while resp not in 'SsNn':
        resp = input('Quer continuar? [S/N] ').strip()[0]
        if resp not in 'SsNn':
            print('Inválido! Tente novamente.')
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Sua lista em ordem crescente: {sorted(lista)}')
