n = int(input('Digite um número para ver sua tabuada: '))
print('-=' * 30)
print(f'Tabuada de {n}'.center(60))
print('-=' * 30)
for c in range(1, 11):
    print(f'{c:3} x {n:3} = {c*n:4}'.center(60))
