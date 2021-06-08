# utf-8
l= []
p = int(input('Digite o primeiro termo: ' ))
r = int(input('Digite a razão: '))
for i in range(0, 10):
    l.append(p)
    p += r
print('Seguem os primeiros dez termos da PA de razão {}:\n{}'.format(r, l))
