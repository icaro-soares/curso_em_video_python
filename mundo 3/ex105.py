def notas(*nota, sit=False):
    """
    :param *nota: recebe várias notas de aluno em uma tupla
    :param opc situação: recebe uma string com a situação da turma, podendo ou não ser exibido
    :var a['total']: recebe o número de notas
    :var a['maior']: recebe a maior nota
    :var a['menor']: recebe a menor nota
    :var a['m']: recebe a média da turma
    :var a['sit']: recebe a situação da turma
    :return a: retorna o dicionário criado
    """
    a = {}
    a['total'] = len(nota)
    a['maior'] = max(nota)
    a['menor'] = min(nota)
    a['m'] = sum(nota)/len(nota)
    if sit:
        if a['m'] >= 7.0:
            a['sit'] = 'BOA'
        elif 5.0 <= a['m'] < 7.0:
            a['sit'] = 'RAZOÁVEL'
        else:
            a['sit'] = 'RUIM'
    return a


resp = notas(5.5, 8, 4.5, 6)
print(resp)
