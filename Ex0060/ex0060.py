'''#utf-8
# Encontrando numero fatorial
n = int(input('Digite um numero pra encontrar o fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')
'''
#utf-8
# Fatorial em for
from math import factorial
n = int(input('Digite o numero que deseja descobrir o fatorial: '))
print('{}! = '.format(n), end='')
for i in range(n, 0, -1):
    print('{}'.format(i), end='')
    print(' X ' if i > 1 else ' = ', end='')
print('{}'.format(factorial(n), end=''))