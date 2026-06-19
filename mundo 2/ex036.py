"""Pergunta o valor de uma casa e diz se o empréstimo está aprovado ou negado
dependendo da porcentagem do salário"""
valor_casa = float(input('Valor da casa: R$'))
salário = float(input('Salário: R$'))
anos = int(input('Anos: '))
valor_prestação = valor_casa / (anos * 12)
print(f'O valor da casa é R${valor_casa:.2f}, seu salário é R${salário:.2f}, serão prestações de R${valor_prestação:.2f}')
if valor_prestação > (salário * 0.30):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
