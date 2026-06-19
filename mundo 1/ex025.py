"""Exibe se o nome da pessoa tem SILVA"""
nome_completo = input('Nome: ').strip().lower()
if 'silva' in nome_completo:
    print('Existe "SILVA" no seu nome!')
else:
    print('Não existe "SILVA" no seu nome!')
