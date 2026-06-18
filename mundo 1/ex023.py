n = int(input('Número [0 a 9999]: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidades: {u}\nDezenas: {d}\nCentena: {c}\nMilhar: {m}')
