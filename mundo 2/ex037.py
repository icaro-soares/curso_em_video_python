núm = int(input('Número inteiro: '))
base = int(input('Escolha a base de conversão: [1 - binário][2 - octal][3 - hexadecimal] '))
if base == 1:
    print(f'{bin(núm)}')
elif base == 2:
    print(f'{oct(núm)}')
elif base == 3:
    print(f'{hex(núm)}')
else:
    print('Escolha inválida!')
