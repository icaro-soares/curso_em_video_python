# Variável que armazena os valores e os soma
s = cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print(f'A soma entre os {cont} valores ímpares no intervalo 1 e 500 é {s}.')
