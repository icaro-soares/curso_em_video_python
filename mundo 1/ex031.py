dist = float(input('Distância (km): '))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print(f'O valor da viagem é R${valor:.2f}'.replace('.', ','))
