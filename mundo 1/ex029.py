"""Exibe o valor de uma multa se o usuário ultrapassar o limite de velocidade"""
vel = float(input('Velocidade do carro (km): '))
if vel > 80:
    multa = (vel - 80) * 7
    print(f'Você foi multado! Valor a pagar R${multa:.2f}'.replace('.', ','))
else:
    print('Pode passar!')
