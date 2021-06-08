#utf-8
#sequencia de números
n = 0
cont = 0
l = []
while n != 999:
    n = int(input('Insira um nº '))
    if n != 999:
        print(n)
    else:
        print('STOP')
    if n != 999:
        cont += 1
        l.append(n)
    if n == 999:
        print('Foram digitados {} números que somam {}.'.format(cont, sum(l)))
