# -*- coding: utf-8 -*-
# exercício 93

dados = dict()
gols = list()

dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(0, partidas):
    gols.append(int(input(f'  Quantos gols na partida {i + 1}? ')))
total = sum(gols)
dados['gols'] = gols[:]
dados['total'] = total
print('-=' * 25)
print(dados)
print('-=' * 25)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 25)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
n = 0
for j in range(1, partidas + 1):
    print(f'  => Na partida {j}, fez {gols[n]} gols.')
    n += 1
print(f'Foi um total de {total} gols.')

