sexo = input('Digite o sexo: [M/F] ').strip()[0]
while sexo not in 'MmFf':
    sexo = input('Inválido, tente novamente. Digite o sexo: [M/F] ')
