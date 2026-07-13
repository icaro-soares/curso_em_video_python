dados = []
temp = []
cont = maior = menor = 0
leves = []
pesadas = []
while True:
    temp.append(input('Nome: ').strip().title())
    temp.append(int(input('Peso (kg): ')))
    cont += 1
    dados.append(temp[:])
    if cont == 1 or temp[1] > maior:
        maior = temp[1]
    if cont == 1 or temp[1] < menor:
        menor = temp[1]
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = input('Continuar? [S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A) Foram cadas cadastradas {len(dados)} pessoas.')
print(f'B) O maior peso foi de {maior}kg.')
print(f'C) O menor peso foi de {menor}kg.')
