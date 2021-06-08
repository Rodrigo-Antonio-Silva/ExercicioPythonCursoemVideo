#utf-8
l = []
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    l.append(n % i)
if l.count(0) == 2:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))
