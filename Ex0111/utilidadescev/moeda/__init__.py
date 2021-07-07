def metade(x=0, formato=False):
    '''
    -> Cálcula a divisão de um determinado preço por dois,
    retornando o resultado com ou sem formatação.
    :param x:
    :param formato:
    :return:
    '''
    res = x / 2
    return res if not formato else moeda(res)


def dobro(x=0, formato=False):
    '''
    -> Cálcula o multiplicação de um determinado preço por dois,
    retornando o resultado com ou sem formatação.
    :param x: o preço que se quer duplicar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = x * 2
    return res if not formato else moeda(res)


def aumentar(x=0, i=0, formato=False):
    '''
    -> Calcula o aumento de um  determinado preço,
    retornando o resultado com ou sem formatação.
    :param x: o preço que se quer reajustar
    :param i: é a porcentagem do aumento.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formato.
    '''
    res = x * (1+(i/100))
    return res if not formato else moeda(res)


def diminuir(x=0, i=0, formato=False):
    '''
    -> Calcula a redução de um determinado preço,
    retornando a resultado com ou sem formatação.
    :param x: o preço que se quer reajustar
    :param i: é a porcentagem de redução.
    :param formato: quer a saída formatada ou não?
    :return: o valor reduzido, com ou sem formato.
    '''
    res = x * (1-(i/100))
    return res if not formato else moeda(res)


def moeda(x=0, moeda='R$ '):
    '''
    -> Realiza as formatações de moeda,
    nos valores informados
    :param x: o preço informado
    :param moeda: incliu o 'R$' indicativo da moeda brasileira.
    :return: as formatações da moeda brasileira.
    '''
    x = f'{x:,.2f}'
    x = x.replace('.', '-')
    x = x.replace(',', '.')
    x = x.replace('-', ',')
    return f'{moeda}{x}'


def resumo(x=0, aum=10, dim=5):
    '''
    -> Realiza a formatação em tabela.
    :param x:o preço informado.
    :param aum:representa a taxa na qual o preço será incrementado.
    :param dim:representa a taxa na qual o preço será reduzido.
    :return:a tabulação dos retornos de todas as funções do grupo moeda.
    '''
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(x)}')
    print(f'Dobro do preço:  \t{dobro(x, True)}')
    print(f'Metade do preço: \t{metade(x, True)}')
    print(f'{aum}% de aumento: \t{aumentar(x, aum, True)}')
    print(f'{dim}% de redução: \t{diminuir(x, dim, True)}')
    print('-' * 30)
