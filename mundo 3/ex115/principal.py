from modulos import interface


while True:
    interface.menu()
    print('-' * 60)
    opc = int(input('Sua opção: '))
    print('-' * 60)
    if opc == 2:
        nome = input('Nome: ').strip().title()
        while True:
            idade = input('Idade: ').strip()
            if idade.isnumeric():
                idade = int(idade)
                interface.linha('Obrigado!')
                break
            else:
                print('Dado inválido!')
    elif opc == 3:
        interface.linha('Saindo...')
        break
    else:
        print('Comando inválido!')
