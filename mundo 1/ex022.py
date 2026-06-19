"""Analisa um nome e mostra as informações sobre ele"""
nome = input('Digite seu nome: ').strip()
print(f'Seu nome escrito em letras maiúsculas: {nome.upper()}')
print(f'Seu nome têm {len(nome)} letras')
nome_separado = nome.split()
print(f'Seu primeiro nome é {nome_separado[0]}, e têm {len(nome_separado[0])} letras')
