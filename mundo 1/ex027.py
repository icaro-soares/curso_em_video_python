"""Exibe apenas o primeiro e o último nome da pessoa"""
nome_completo = input('Nome completo: ').strip()
print(f'Seu primeiro nome é {nome_completo.split()[0]}')
print(f'Seu último nome é {nome_completo.split()[-1]}')
