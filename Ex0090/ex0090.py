# -*- coding: utf-8 -*-
# exercício 90

alunos = dict()

alunos['nome'] = str(input('Nome: '))
alunos['media'] = float(input('Média: '))

if 5 <= alunos["media"] < 7:
    alunos["situacao"] = 'Recuperação'
elif alunos["media"] < 5:
    alunos['situacao'] = 'Reprovado'
else:
    alunos["situacao"] = 'Aprovado'
print('-=' * 21)
for k, v in alunos.items():
    print(f' -{k} é igual a {v}')
