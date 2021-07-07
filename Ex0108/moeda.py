def metade(x=0):
    x = x / 2
    return x


def dobro(x=0):
    x = x * 2
    return x


def aumentar(x=0, i=0):
    x = x * (1+(i/100))
    return x


def diminuir(x=0, i=0):
    x = x * (1-(i/100))
    return x


def moeda(x=0, moeda='R$ '):
        x = f'{x:,.2f}'
        x = x.replace('.', '-')
        x = x.replace(',', '.')
        x = x.replace('-', ',')
        return f'{moeda}{x}'



