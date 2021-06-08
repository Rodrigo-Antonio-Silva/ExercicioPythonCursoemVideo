#utf-8
l = []
for i in range(1, 6):
    l.append(float(input('Informe o peso da {}ª pessoa: '.format(i))))

from functools import reduce
print('='*36)

print('O maior peso informado foi {} kg.'.format(reduce((lambda x,y: x if(x > y) else y), l)))
print('O menor peso informado foi {} kg.'.format(reduce((lambda x,y: x if(x < y) else y),l)))

