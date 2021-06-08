n = int(input('Você deseja somar os números impares multiplos de tres até de 1 até: '))
soma = 0
cont = 0
for c in range(1, n, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores será: {}'.format(cont, soma))

