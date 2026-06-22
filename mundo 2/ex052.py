from time import sleep


núm = int(input('Digite um número inteiro qualquer: '))
s = 0
print(f'Analisando...')
sleep(1)
for c in range(1, núm+1):
    if núm % c == 0:
        s += 1
print(f'O número {núm} é divisível por {s} valores. ', end='')
if s == 2:
    print(f'É primo.')
else:
    print(f'Não é primo.')
