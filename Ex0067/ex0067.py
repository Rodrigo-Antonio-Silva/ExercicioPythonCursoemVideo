while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 33)
    if n > 0:
        x = 0
        while x <= 10:
            print(f'{n} X {x} = {n*x}')
            x += 1
        print('-'* 33)
    else:
        print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
        break