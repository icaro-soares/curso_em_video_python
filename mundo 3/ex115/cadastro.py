from time import sleep
from cadastro import interface

while True:
    interface
    menu = int(input('''    1. Ver pessoas cadastradas
    2. Cadastrar pessoas
    3. Sair do sitema: '''))
    print('-' * 30)
    match menu:
        case 2:
            nome = input('Nome: ').strip().title()
            idade = int(input('Idade: '))
        case 3:
            print('Saindo...')
            sleep(1)
            print('Obrigado por utilizar!')
            break
        case _:
            print('Opção inválida! Tente novamente.')
