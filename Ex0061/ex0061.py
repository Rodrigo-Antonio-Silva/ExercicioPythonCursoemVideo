p = int(input('Digite o primeiro termo: ' ))
r = int(input('Digite a razão: '))
s = p
x = 0
while x < 10:
    print(p, end='')
    print(end=' → ' if x < 9 else print(end=' → FIM'))
    p += r
    x += 1

print('Acima os primeiros dez termos da PA de razão {} e primeiro termo {}.'.format(r, s))
