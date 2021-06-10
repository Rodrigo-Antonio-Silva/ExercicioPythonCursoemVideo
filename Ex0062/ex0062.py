# utf-8
# PA

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
termos = int(input('Digite quantos termos deseja ver: '))

res1 = 0
x = 0
while True:
    while x < termos:
        print(termo1, end='')
        print(end=' → ' if x < termos -1 else print(end=' → PAUSA'))
        termo1 += razao
        x += 1
    y = 0
    res = int(input('Deseja quantos termos mais: '))
    res1 += res
    if res != 0:
        while y < res:
            print(termo1, end='')
            print(end=' → ' if y < res - 1 else print(end=' → PAUSA'))
            termo1 += razao
            y += 1
    else:
        print('Progressão finalizada com {} termos mostrados.'.format(termos+res1))
        break



