# utf-8
# exercício 98
from time import sleep


def linha():
    print('-=' * 21)


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(0.3)
    if inicio < fim and passo > 0:
        while inicio <= fim:
            print(inicio, end=' ')
            inicio += passo
            sleep(1)
        print('FIM!')
    else:
        if passo > 0:
            while inicio >= fim:
                print(inicio, end=' ')
                inicio -= passo
                sleep(1)
            print('FIM!')
        elif passo < 0 and inicio > fim:
            while inicio >= fim:
                print(inicio, end=' ')
                inicio += passo
                sleep(1)
            print('FIM!')
        elif passo < 0 and inicio < fim:
            passo = passo * (-1)
            while inicio <= fim:
                print(inicio, end=' ')
                inicio += passo
                sleep(1)
            print('FIM!')


linha()
contador(1, 10, 1)
linha()
contador(10, 0, 2)
linha()
print('Agora é a sua vez de personalizar a contagem!')
start = int(input('Inicio: '))
end = int(input('Fim: '))
step = int(input('Passo: '))
linha()
contador(start, end, step)

