p = int(input('Digite o primeiro termo: ' ))
r = int(input('Digite a razão: '))
s = p
x = 0
while x < 10:
    if x == 9:
        print(p)
        break
    print(p, end='-')
    p += r
    x += 1
print('Acima os primeiros dez termos da PA de razão {} e primeiro termo {}.'.format(r, s))
