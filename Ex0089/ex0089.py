# utf-8
# exercício 89

from statistics import mean
from time import sleep
boletim = list()
x = 0
y = 1
while True:
    nome = str(input('Nome: '))
    boletim.append([nome])
    boletim[x].append(list())
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    boletim[x][y].append(nota1)
    boletim[x][y].append(nota2)
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    x += 1
    if resp == 'N':
        break
print('-=' * 27)
print(f'{"Nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('-' * 27)
z = 0
for i in boletim:
    print(f'{boletim.index(i):<4}', end='  ')
    print(f'{boletim[z][0]:<10}', end='      ')
    print(f'{mean(boletim[z][1]):8>.1f}')
    z += 1
print('-' * 27)
while True:
    cont = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    if cont == 999:
        print('Finalizando...')
        sleep(1.3)
        print('<<<< VOLTE SEMPRE >>>>')
        break
    else:
        print(f'Notas de {boletim[cont][0]} são {boletim[cont][1]}')
print('-' * 27)
