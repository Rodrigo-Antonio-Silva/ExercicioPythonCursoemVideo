# -*- coding: utf-8 -*-
# exercício 91

from random import randint
from time import sleep

print('Valores sorteados:')
jogadores = dict()
for i in range(1, 5):
    valor = randint(1, 6)
    jogadores['jogador' + str(i)] = valor
for k, v in jogadores.items():
    print(f'   O {k} tirou {v}.')
    sleep(1)
print('-=' * 21)
print('Ranking dos jogadores:')
n = 1
for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'   {n}º lugar: {i} com {jogadores[i]}.')
    sleep(1.2)
    n += 1
