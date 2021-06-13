#utf-8
#sequencia de números

import numpy as np

while True:
    n = 0
    l = []
    while n != 999:
        n = int(input('Insira um nº [999 para parar]: '))
        if n == 999:
            print('=========== PAUSA! ===================')
        if n != 999:
            l.append(n)
        if n == 999:
            print('Foram digitados {} valores sua média foi {:.2F}, sua soma {:.2F}, o maximo {:.2F} e o minimo {:.2F}.'.format(len(l), np.mean(l), np.sum(l), np.max(l), np.min(l)))
    cont = str(input('Deseja contiuar? [S/N]:')).upper()
    if cont == 'N':
        print('========= FIM! =========')
        break
    else:
        continue

