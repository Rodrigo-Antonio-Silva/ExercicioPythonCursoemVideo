# utf-8
# exercicio 79

times = ('Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Atlético-MG',	'Bragantino', 'Fluminense', 'Bahia', 'Palmeiras',
         'Corinthians', 'Ceará', 'Santos', 'Internacional',	'Juventude', 'Cuiabá','Sport', 'São Paulo', 'Chapecoense', 'Grêmio', 'América-MG')
print('{: ^40}'.format('BRASILEIRÃO 2021'))
print(times)
print('-=' * 21)
print(f'Os5 primeiros são {times[0:5]}')
print('-=' * 21)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 21)
print(f'Times em ordem alfabética {sorted(times)}')
print('-=' * 21)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
