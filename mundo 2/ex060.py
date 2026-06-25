n = int(input('Digite um número para ver seu fatorial: '))
m = 1
while n > 0:
    if n > 1:
        print(f'{n}! x', end=' ')
    else:
        print(f'{n}! =', end=' ')
    m *= n
    n -= 1
print(f'{m}')
