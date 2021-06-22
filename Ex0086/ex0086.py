# utf-8
# exercício 86

matrix = list()
linha1 = list()
linha2 = list()
linha3 = list()

matrix.append(linha1)
matrix.append(linha2)
matrix.append(linha3)

for i in range(0, 3):
    a = int(input(f'Digite um valor para [0, {i}]: '))
    matrix[0].append(a)
for j in range(0, 3):
    b = int(input(f'Digite um valor para [1, {j}]: '))
    matrix[1].append(b)
for l in range(0, 3):
    c = int(input(f'Digite um valor para [2, {l}]: '))
    matrix[2].append(c)
print('-=' * 15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('-=' * 15)





