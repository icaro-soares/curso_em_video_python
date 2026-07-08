lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ').strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'A) Foram digitados {len(lista)} números')
print(f'B) Lista em ordem decrescente: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('C) O valor 5 está na lista.')
else:
    print('C) O valor 5 não está na lista.')
