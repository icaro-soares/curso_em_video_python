termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
c = 1
#termo = primeiro + (10 - 1) * razão
while c <= 10:
    print(f'{termo} ', end='')
    termo += razão
    c += 1
