# utf-8
# exercício 88

from random import randint
from time import sleep

apostas = list()
print('=' * 21)
print('{0:^21}'.format('JOGA NA MEGA SENA'))
print('=' * 21)
num = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-= SORTEANDO {num} JOGOS -=-=-=-=')
for i in range(0, num):
    apostas.append([])
    for j in (range(0, 6)):
         while True:
            r = randint(1, 61)
            if r not in apostas[i]:
                apostas[i].append(r)
                break
    apostas[i].sort()
    print(f'Jogo {i + 1}: {apostas[i]}')
    sleep(1.5)
print('-=-=-=-=-=< BOA SORTE! >-=-=-=-=-=-=')
