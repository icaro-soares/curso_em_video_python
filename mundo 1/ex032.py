from datetime import date


ano = int(input('Ano [0 p/ o ano atual: '))
atual = date.today().year
if ano == 0:
    ano = atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é Bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
