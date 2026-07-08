lista = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ').strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Sua lista completa: {sorted(lista)}')
print(f'Lista de pares: {sorted(pares)}')
print(f'Lista de ímpares: {sorted(impares)}')
