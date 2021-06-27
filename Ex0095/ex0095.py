# -*- coding: utf-8 -*-
# exercício 95
estatisticas = list()
gols = list()
while True:
    n = {}
    n['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {n["nome"]} jogou? '))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    total = sum(gols)
    n['gols'] = gols[:]
    n['total'] = total
    estatisticas.append(n.copy())
    gols.clear()
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while True:
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    if resp == 'N':
        break
print('-=' * 21)
print('cod ', end='')
for i in n.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 42)
for k, v in enumerate(estatisticas):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 42)
while True:
    atleta = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if atleta >= len(estatisticas) and atleta < 999:
        print(f'ERRO! Não existe jogador com código {atleta}! Tente novamente.')
    elif atleta < len(estatisticas):
        print(f'--LEVANTAMENTO DO JOGADOR {estatisticas[atleta]["nome"]}:')
        for j in range(0, len(estatisticas[atleta]["gols"])):
            print(f'  No jogo {j + 1} fez {estatisticas[atleta]["gols"][j]} gols.')
    elif atleta == 999:
        print('<<< VOLTE SEMPRE! >>>')
        break
