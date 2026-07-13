dados = []
temp = []
while True:
    temp.append(input('Nome: ').strip().title())
    temp.append(int(input('Peso (kg): ')))
    dados.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = input('Continuar? [S/N] ').strip()[0]
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'A) Foram cadas cadastradas {len(dados)} pessoas.')