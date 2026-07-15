matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
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
    soma_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'B) Soma dos valores da segunda coluna: {soma_coluna}')
maior_linha = max(matriz[2])
print(f'C) O maior valor da terceira linha: {maior_linha}')
