matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_coluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor ({l}, {c}): '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A) A soma dos pares é: {soma_pares}')
for l in range(0, 3):
    soma_coluna += matriz[l][c]
print(f'B) Soma dos valores da segunda coluna: {soma_coluna}')
for c in range(0, 3):
    if c == 1 or matriz[1][c] > maior_coluna:
        maior_coluna = matriz[1][c]
print(f'C) O maior valor da terceira coluna: {maior_coluna}')
