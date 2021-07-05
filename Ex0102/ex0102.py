# utf-8
# exercício 102


def fatorial(n, show=True):
    """
    => calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) mostra ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    from time import sleep
    f = 1
    print(f'\nO fatorial de {n} é: ')
    sleep(0.5)
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(f' x ', end='')
            elif 1 == 1:
                print(f' = ', end='')
    return f


n = int(input('Digite um numero: '))
print(fatorial(n))
print('-=' * 15)
