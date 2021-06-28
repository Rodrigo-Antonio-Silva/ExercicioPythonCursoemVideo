# -*- coding: utf-8 -*-
# exercício 94

dados = list()
n = 0

while True:
    n = {}
    n['nome'] = str(input('Nome: '))
    while True:
        n['sexo'] = str(input('Sexo:[M/F] ')).upper().strip()[0]
        if n['sexo'] not in 'MF':
            print('ERRO! Responda apenas M ou F.')
        else:
            break
    n['idade'] = int(input('Idade: '))
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    dados.append(n.copy())
    if resp != 'S':
        break
print('-=' * 24)
print(f'- O grupo tem {len(dados)} pessoas.')
somaid = 0
for d in dados:
    for k, v in d.items():
        if k == 'idade':
            somaid += v
media = somaid/len(dados)
print(f'- A média de idade é de {media:5.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for d in dados:
    if d['sexo'] == 'F':
        print(d['nome'], end='  ')
print()
print(f'- Lista de pessoas que estão acima da média: ',end='')
print()
for d in dados:
    if d['idade'] >= media:
        print('   ', end='')
        for k, v in d.items():
            print(f'   {k:<3} = {v}; ', end='')
        print()
print('-=' * 24)
print('<<< ENCERRADO >>>')

