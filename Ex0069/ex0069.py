#utf-8
#exercício 69

print('============= INÍCIO DO PROGRAMA ===============')
countId = 0
countSx = 0
countM20 = 0
while True:
    print('-' * 21)
    print('CADASTRE UMA PESSOA')
    print('-' * 21)
    idade = int(input('Idade: '))
    while True:
        sexo = str(input('Sexo: [M/F]: ')).upper().strip()[0]
        if sexo == 'M' or sexo == 'F':
            break
    print('-' * 21)
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if resp == 'S' or resp == 'N':
            break
    if idade > 18:
        countId += 1
    if sexo == 'M':
        countSx += 1
    if sexo == 'F' and idade < 20:
        countM20 += 1
    if resp == 'N':
        print('============= FIM DO PROGRAMA ===============')
        print(f'Total de pessoas com mais de 18 anos: {countId}.')
        print(f'Ao todo temos {countSx} homens cadastrados.')
        print(f'E temos {countM20} mulheres com menos de 20 anos.')
        break