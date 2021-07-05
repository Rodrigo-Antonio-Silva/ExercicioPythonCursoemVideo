# utf-8
# exercício 103


def ficha(name='<desconhecido>', score=0):
    print(f'O jogador {name} fez {score} gol(s) no campeonato.')


# programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(score=g)
else:
    ficha(n, g)
