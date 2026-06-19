"""Simula um mercado"""


def desconto_dinheiro(preço):
    """Calcula o desconto de 10%"""
    preço_desc = preço - (preço * 0.10)
    return preço_desc

def desconto_cartão(preço):
    """Calcula o desconto de 5%"""
    preço_desc = preço - (preço * 0.05)
    return preço_desc

def juros_cartão(preço):
    """Calcula juros de 20%"""
    preço_juros = preço + (preço * 0.20)
    return preço_juros

preço = float(input('Valor: R$'))
print('-=' * 30)
pgt = int(input('Opção de pgt: '
                '[1 - à vista dinheiro/cheque]'
                '[2 - à vista cartão]'
                '[3 - até 2x no cartão]'
                '[4 - 3x ou mais no cartão] '))
match pgt:
    case 1:
        print('À vista dinheiro ou cheque desconto 10%')
        preço_final = desconto_dinheiro(preço)
        print(f'O valor com desconto é R${preço_final:.2f}')
    case 2:
        print('À vista cartão desconto 5%')
        preço_final = desconto_cartão(preço)
        print(f'O valor com desconto é R${preço_final:.2f}')
    case 3:
        print('Até 2x no cartão preço normal')
        parc = int(input('Quantas parcelas: [até 2x] '))
        if parc not in range(1, 3):
            print('Opção inválida!')
            quit()
        preço_parc = preço / parc
        print(f'Serão {parc} parcelas de R${preço_parc:.2f}')
    case 4:
        print('3x ou mais no cartão juros 20%')
        parc = int(input('Quantas parcelas: [3x ou mais] '))
        if parc < 3:
            print('Opção inválida!')
            quit()
        preço_final = juros_cartão(preço)
        preço_parc = preço_final / parc
        print(f'O valor final é R${preço_final:.2f} e serão {parc} parcelas de '
              f'R${preço_parc}')
    case _:
        print('Opção inválida!')
        quit()
