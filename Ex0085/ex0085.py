# utf-8
# exercício

num = list()
par = list()
impar = list()
num.append(par)
num.append(impar)
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print('-=' * 30)
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

