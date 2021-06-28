# utf-8
# exrecício 96


def dim(larg, alt):
    d = larg * alt
    print(f'A área de um terreno {larg} X {alt} é de {d}m².')


# Programa principal
print(' CONTROLE DE TERRENOS')
print('-' * 15)
l = float(input('LARGURA (m): '))
a = float(input('COMPRIMENTO (m): '))
dim(l, a)

