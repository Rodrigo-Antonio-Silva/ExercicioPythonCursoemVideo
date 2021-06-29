# utf-8
# exercício 100
from random import randint
from time import sleep
numeros = list()


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(5):
        numeros.append(randint(1, 10))
        print(numeros[-1], end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma(lista):
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    par = 0
    for i in numeros:
        if i % 2 == 0:
            par += i
    print(par)


sorteia(numeros)
soma(numeros)

