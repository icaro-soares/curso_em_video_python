# Primeira forma lendo todos os valores
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print()
# Segunda forma usando menos memória
for c in range(2, 51, 2):
    print(c, end=' ')
