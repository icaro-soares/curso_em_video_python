def maior(*n):
    print('Analisando valores passados...')
    if len(n) > 0:
        for num in n:
            print(num, end=' ')
        print(f'\nForam informados {len(n)} valores.')
        print(f'O maior valor é {max(n)}')
    elif len(n) <= 0:
        print('Nenhum valor foi informado.')
    print('-=' * 30)


maior(5, 4, 6, 0)
maior(3, 9)
maior(10, 20, 30, 35)
maior()
print('Sua vez')
