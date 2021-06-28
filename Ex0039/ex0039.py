# coding utf-8
# informando a idade

from datetime import datetime

now = datetime.now()
nasc = int(input('Em que ano você nasceu? '))
s = str(input('Informe o sexo: '))
idade = now.year - nasc
if s =='f':
    print('Pessoas do sexo feminino não devem se alistar.')
else:
    pass
    if idade < 18:
        print('Quem nasceu em {} tem {} anos.\nAinda faltam {} anos pro alistamento.\n'
          'Seu alistamento será em {}.'.format(nasc, idade, 18 - idade, nasc + 18))
    elif idade == 18:
        print('{} anos é hora de se alistar IMEDIATAMENTE!'.format(idade))
    else:
        print('Com {} anos já se passaram {} anos do tempo do alistamento.\nSeu ano de alistamento foi em {}.'
          .format(idade, idade - 18, nasc +18))

