# utf-8
# exercício 106
from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',   # 1 - vermelho
     '\033[0;30;42m',   # 2 - verde
     '\033[0;30;43m',   # 3 - amarelo
     '\033[0;30;44m',   # 4 - azul
     '\033[0;30;45m',   # 5 - roxo
     '\033[0;30;46m',   # 6 - verde?
     '\033[7;30m'       # 7 - branco
     );


def ajuda(resp):
    titulo(f'Acessando o manual do comando \'{resp}\'', 4)
    print(c[7], end='')
    help(resp)
    print(c[0], end='')
    sleep(0.5)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.5)

# programa principal
f = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    f = (str(input('Biblioteca/Função: ')))
    if f.upper() == 'FIM':
      break
    else:
        ajuda(f)
titulo('ATÉ LOGO!', 1)
