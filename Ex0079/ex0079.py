# utf-8
# exercício 79

num = list()
while True:
    while True:
        valor = input('Digite um valor: ')
        if valor.isnumeric():
            valor = int(valor)
            break
    if valor not in num:
        num.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-=' * 21)
print(f'Você digitou os valores {sorted(num)}')




