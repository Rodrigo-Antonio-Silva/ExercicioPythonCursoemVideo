# coding utf-8
# verificação categoria do atleta
from datetime import datetime

nasc = int(input('Qual a data de nascimento: '))
now = datetime.now()
ano_nasc = now.year - nasc
print('O atleta tem {} anos.'.format(now.year - nasc))
if ano_nasc <= 9:
    print('Sua categoria será: MIRIM')
elif ano_nasc <= 14:
    print('Sua categoria será: INFANTIL')
elif ano_nasc <= 19:
    print('Sua categoria será: JUNIOR')
elif ano_nasc == 20:
    print('Sua categoria será: SÊNIOR')
else:
    print('Sua categoria será: MASTER')
