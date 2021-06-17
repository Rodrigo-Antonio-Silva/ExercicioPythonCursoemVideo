# utf-8
# exercício 82
compl = list()
pares = list()
impar = list()
while True:
    while True:
        valores = input('Digite um número: ')
        if valores.isnumeric():
            valores = int(valores)
            compl.append(valores)
        break
    while True:
        resp = input('Quer continuar? [S/N]: ').upper().strip()[0]
        if resp in 'SN':
            break
    if resp != 'S':
        break
print('-=' * 27)
print(f'A lista comleta é {compl}')
for i in compl:
    if i % 2 == 0:
        pares.append(i)
    else:
        impar.append(i)
print(f'A lista de pares é {pares}')
print(f'Alista de impares é {impar}')
