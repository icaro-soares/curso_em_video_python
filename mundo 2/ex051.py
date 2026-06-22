inicio = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
print('Mostrando os dez primeiros termos da PA')
# Fórmula para descobrir o décimo termo
décimo = inicio + (11 - 1) * razão
for c in range(inicio, décimo, razão):
    print(c, end=' ')
