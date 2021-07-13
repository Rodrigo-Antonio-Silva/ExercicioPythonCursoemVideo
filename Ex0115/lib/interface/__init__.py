def Leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mErro: por favor, digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu():
    cabecalho('MENU PRINCIPAL')
    print('\33[0;33m1\33[m - \33[0;34mVer pessoas cadastradas\33[m')
    print('\33[0;33m2\33[m - \33[0;34mCadastrar nova pessoa\33[m')
    print('\33[0;33m3\33[m - \33[0;34mSair do Sistema\33[m')





