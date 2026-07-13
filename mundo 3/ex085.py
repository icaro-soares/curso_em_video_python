números = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º valor: '))
    números[0].append(n) if n % 2 == 0 else números[1].append(n)
print('-=' * 30)
números[0].sort()
números[1].sort()
print(f'Lista: {números}')
