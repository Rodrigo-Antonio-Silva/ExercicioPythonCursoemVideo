# -*- coding: utf-8 -*-
# exercício 92

from datetime import date

ano_atual = date.today()
anoatual= ano_atual.year
cadastro = dict()

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
cadastro['idade'] = (anoatual - nasc)
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salário: R$ '))
    cadastro['aposentadoria'] = (35 + cadastro['contratação']) - nasc
print(cadastro)
print('-=' * 30)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')