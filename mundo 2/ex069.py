mais_dezoito = homens = mulheres_menos_20 = 0
while True:
    idade = ' '
    while True:
        idade = int(input('Idade: '))
        if idade < 0:
            print('Idade inválida, digite novamente!')
        else:
            break
    if idade > 18:
        mais_dezoito += 1
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = input('Sexo: [M/F] ').strip()[0]
        if sexo not in 'MmFf':
            print('Inválido, digite novamente!')
    if sexo in 'Mm':
        homens += 1
    if idade < 20 and sexo in 'Ff':
        mulheres_menos_20 += 1
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ').strip()[0]
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Pessoas com mais de dezoito anos: {mais_dezoito}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de vinte anos: {mulheres_menos_20}')
