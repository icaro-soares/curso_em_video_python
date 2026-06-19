"""Pergunta um salário e dá o aumento dependendo do valor"""
sal = float(input('Salário: R$'))
print(f'Salário atual: R${sal:.2f}'.replace('.', ','))
if sal > 1_250:
    novo_sal = sal + (sal * 0.10)
else:
    novo_sal = sal + (sal * 0.15)
print(f'Salário com aumento: R${novo_sal:.2f}'.replace('.', ','))
