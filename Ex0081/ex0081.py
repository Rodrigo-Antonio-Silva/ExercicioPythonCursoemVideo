# utf-8
# exercício 81

lista = list()
while True:
    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric():
            valor = int(valor)
            lista.append(valor)
            break
    while True:
        resp = str(input(f'Você quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp != 'S':
        break
print('-=' * 27)
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 not in lista:
    print(f'O valor 5 não foi encontrado na lista!')
else:
    print(f'O valor 5 foi encontrado na lista!')
