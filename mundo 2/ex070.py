tot = mais_1000 = barato = c = 0
produto_barato = ' '
while True:
    nome = ' '
    while True:
        nome = input('Nome do produto: ').strip().title()
        if len(nome) <= 0:
            print('Você precisa digitar o nome do produto.')
        else:
            break
    preço = ' '
    while True:
        preço = float(input('Valor: R$'))
        if preço < 0:
            print('Valor inválido, tente novamente.')
        else:
            break
    c += 1
    tot += preço
    if preço > 1_000:
        mais_1000 += 1
    if c == 1:
        barato = preço
        produto_barato = nome
    else:
        if preço < barato:
            barato = preço
            produto_barato = nome
    r = ' '
    while r not in 'SsNn':
        r = input('Quer continuar? [S/N] ').strip()[0]
        if r not in 'SsNn':
            print('Resposta inválida.')
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Total gasto na compra: R${tot:.2f}'.replace('.', ','))
print(f'Produtos que custam mais de R$1.000,00: {mais_1000}')
print(f'O produto mais barato é {produto_barato} e custa R${barato:.2f}')
