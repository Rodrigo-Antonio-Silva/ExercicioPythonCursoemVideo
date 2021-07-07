def metade(x, t=False):
    x = x / 2
    return x


def dobro(x, t=False):
    x = x * 2
    return x


def aumentar(x, i, t=False):
    x = x * (1+(i/100))
    return x


def diminuir(x, i, t=False):
    x = x * (1-(i/100))
    return f'{x}'
