from modulos import interface


while True:
    interface.menu()
    opc = int(input('Sua opção: '))
    print('-' * 60)
    if opc == 2:
        nome = input('Nome: ').strip().title()
        idade = int(input('Idade: '))
    elif opc == 3:
        print('Saindo...')
        break
    else:
        print('Comando inválido')
