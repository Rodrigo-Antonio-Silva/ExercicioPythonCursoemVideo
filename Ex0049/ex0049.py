t = int(input('Digite um número para ver sua tabuada: '))
for i in range(1, 11):
    print('{} {} {} {} {}'.format(t, 'X', i, '=', (t * i)))

print('Fim')