valores = (
        int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: ')), int(input('Digite um valor: '))
)
print(f'O número 9 apareceu {valores.count(9)} vez(es).')
if 3 in valores:
    print(f'O número 3 apreceu pela primeira vez na posição {valores.index(3)+1}')
else:
    print('O valor 3 não apareceu na tupla.')
print('Valores pares: ', end='')
for v in valores:
    if v % 2 == 0:
        print(f'[{v}] ', end='')
