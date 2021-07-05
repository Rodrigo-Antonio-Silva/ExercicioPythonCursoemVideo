# utf-8
# exercício 105


print('-' * 30)


def notas(*n, sit=None):
    """
notas(*n, sit=None)
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    aluno = dict()
    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['média'] = sum(n)/len(n)
    if sit:
        if aluno['média'] < 5:
            aluno['situação'] = 'RUIM'
        elif 5 <= aluno['média'] < 7:
            aluno['situação'] = 'RAZOAVEL'
        else:
            aluno['situação'] = 'BOA'
    return aluno


resp = (notas(5.5, 2.5, 1.5, sit=True))
help(notas)
print(resp)
