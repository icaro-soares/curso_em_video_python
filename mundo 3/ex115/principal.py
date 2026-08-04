from modulos import interface, arquivo


while True:
    interface.menu()
    print('-' * 60)
    opc = int(input('Sua opção: '))
    print('-' * 60)
    if opc == 1:
        interface.linha('Mostrando pessoas cadastradas...')
        if arquivo.arquivoExiste('cursoemvideo.txt'):
            print('Tudo ok!')
        else:
            print('Criando arquivo...')
            arquivo.criarArquivo('cursoemvideo.txt')
    elif opc == 2:
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
