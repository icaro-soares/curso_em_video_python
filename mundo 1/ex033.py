n1 = int(input('1º número: '))
maior = n1
n2 = int(input('2º número: '))
if n2 > maior:
    maior = n2
n3 = int(input('3º número: '))
if n3 > maior:
    maior = n3
print(f'O maior valor é {maior}')
