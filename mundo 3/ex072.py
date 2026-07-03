números = (
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
)
while True:
        n = int(input('Digite um número: [0 a 20] '))
        if n not in range(0, 21):
                print('Opção inválida!')
        else:
                break
print(f'Você digitou o número {números[n]}')
