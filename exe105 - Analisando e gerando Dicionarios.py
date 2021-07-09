def notas(*num, sit=False):
    """
    -> Função que analiza notas e situações de vários alunos
    :param num: notas, aceita várias
    :param sit: situação do aluno, parametro opcional
    :return: dicionário com várias informações sobre a situação do aluno
    """

    resultado = dict()
    resultado['maior'] = max(num)
    resultado['menor'] = min(num)
    resultado['total'] = len(num)
    resultado['média'] = sum(num) / len(num)
    if sit:
        if resultado['média'] >= 7:
            resultado['situação'] = 'Aprovado'
        elif resultado['média'] >= 5:
            resultado['situação'] = 'Recuperação'
        else:
            resultado['situação'] = 'Reprovado'

    return resultado


# Programa principal
resp = notas(2.2, 3.7, 1.5, sit=True)
print(resp)
help(notas)
