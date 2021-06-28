#utf-8
# Fatorial em for

from math import factorial
n = int(input('Digite o numero que deseja descobrir o fatorial: '))
print('{}! = '.format(n), end='')
for i in range(n, 0, -1):
    print('{}'.format(i), end='')
    print(' X ' if i > 1 else ' = ', end='')
print('{}'.format(factorial(n), end=''))