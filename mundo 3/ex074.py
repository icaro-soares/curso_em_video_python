from random import randint

núm = (
        randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
)
print('Valores: ', end='')
for n in núm:
    print(n, end=' ')
print(f'\nO maior valor da tupla é {max(núm)}\nE o menor valor é {min(núm)}')
