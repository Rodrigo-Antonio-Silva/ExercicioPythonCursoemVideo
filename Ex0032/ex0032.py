#coding utf-8
#código que verifica se o ano sugerido pelo usuário é bisexto.
from datetime import date
a = int(input('Que ano quer analisar? Coloque 0 para analisar o número atual: '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano \33[34m{}\33[m é Bissexto.'.format(a))
else:
    print('O ano \33[31m{}\33[m não é Bissexto.'.format(a))
