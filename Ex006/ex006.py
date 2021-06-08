print('=' * 24)
n = int(input('\33[4mDigite um número:\33[m '))
print('=' * 24)
print('\33[33mSeu dobro de {} é {},\33[m \n\33[36mseu triplo é {},\33[m \n\33[31me sua raiz quadrada é {:.0f}.\33[m'.format(n, (n*2), (n*3), (n**0.5)))
print('=' * 24)


