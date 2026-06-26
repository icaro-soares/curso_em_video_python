s = m = c = maior = menor = 0
while True:
    n = int(input('Digite um número: '))
    s += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = ' '
    while continuar not in 'SsNn':
        continuar = input('Quer continuar? [S/N] ').strip()[0]
        if continuar not in 'SsNn':
            print('Inválido! Digite novamente!')
    if continuar in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {c} valores.')
m = s / c
print(f'A média entre eles é {m:.1f}.')
print(f'O maior valor é {maior}. O menor valor é {menor}.')
