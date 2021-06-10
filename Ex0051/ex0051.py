# utf-8

p = int(input('Digite o primeiro termo: ' ))
r = int(input('Digite a razão: '))
count = 0

for i in range(10):
    print(p, end='')
    print(end=' → ' if count < 9 else print(end=' → FIM'))
    p += r
    count += 1
