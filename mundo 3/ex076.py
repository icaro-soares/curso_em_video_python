produtos = (
        'tv', 1_700.00,
        'smartphone', 3_500.00,
        'tablet', 1_699.99,
        'notebook', 6_899.99,
)
print('Produtos'.center(30))
print('='*30)
for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:<15}', end='')
    else:
        preço_formatado = f'R$ {produtos[pos]:.2f}'.replace('.', ',')
        print(f'{preço_formatado:>15}')
print('=' * 30)
