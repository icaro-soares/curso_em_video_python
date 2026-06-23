soma_idade = media_grupo = homem_mais_velho = mulheres_menos_20 = 0
nome_homem_mais_velho = ''
for c in range(1, 5):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').strip().upper()[0]
    print('-=' * 30)
    soma_idade += idade
    if c == 1 and sexo == 'M':
        homem_mais_velho = idade
        nome_homem_mais_velho = nome
    else:
        if idade > homem_mais_velho:
            homem_mais_velho = idade
            nome_homem_mais_velho = nome
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1
media_grupo = soma_idade/4
print(f'A média de idade do grupo é de {media_grupo:.0f} anos.')
print(f'O homem mais velho se chama {nome_homem_mais_velho} e têm '
      f'{homem_mais_velho} anos.')
print(f'Mulheres com menos de 20 anos: {mulheres_menos_20}.')
