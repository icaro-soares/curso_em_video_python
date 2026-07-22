from datetime import date


atual = date.today().year


def voto(nascimento):
    """
    Calcula a idade da pessoa e retorna se o voto é obrigatório
    :PARAM: nascimento, ano que a pessoa nasceu
    """
    if (atual - nascimento) >= 18:
        return 'OBRIGATÓRIO'
    elif 16 <= (atual - nascimento) < 18:
        return 'OPCIONAL'
    else:
        return 'NEGADO'
    
    

nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Sua idade é {idade}. Voto: {voto(nasc)}')
