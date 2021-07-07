def metade(x=0, formato=False):
    res = x / 2
    return res if not formato else moeda(res)


def dobro(x=0, formato=False):
    res = x * 2
    return res if not formato else moeda(res)


def aumentar(x=0, i=0, formato=False):
    res = x * (1+(i/100))
    return res if not formato else moeda(res)


def diminuir(x=0, i=0, formato=False):
    res = x * (1-(i/100))
    return res if not formato else moeda(res)


def moeda(x=0, moeda='R$ '):
        x = f'{x:,.2f}'
        x = x.replace('.', '-')
        x = x.replace(',', '.')
        x = x.replace('-', ',')
        return f'{moeda}{x}'

