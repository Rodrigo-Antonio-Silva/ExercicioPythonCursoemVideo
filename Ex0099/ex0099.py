# utf-8
# exercício 99

from time import sleep


def maior(*num):
    max = cont = 0
    print('-=' * 27)
    print('Analisando os valores passados...')
    sleep(1)
    for valor in num:
        print(f'{valor}', end=' ')
        sleep(0.5)
        if cont == 0:
            max = valor
        else:
            if valor > max:
                max = valor
        cont += 1
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
