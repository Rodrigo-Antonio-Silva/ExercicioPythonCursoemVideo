n = int(input('Digite um número para ver sua tabuada: '))
a = len(range(1, 11))
x = 1
print('-' * 32)
while x <= a:
    p = n * x
    print('\33[33m{}\33[m \33[31mX\33[m \33[36m{}\33[m = \33[4m{}\33[m'.format(n, x, p))
    x = x + 1
print('-' * 32)
