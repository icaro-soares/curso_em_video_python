import os


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = soma_coluna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
os.system('cls' if os.name == 'nt' else 'clear')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
