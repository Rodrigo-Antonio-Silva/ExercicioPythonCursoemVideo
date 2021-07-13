# utf-8
# exercício 114

from urllib.request import urlopen
try:
    html = urlopen('http://pudim.com.br/')
    if html.read():
        print('\033[0;33mConsegui acessar o site Pudim com sucesso.\033[m')
except:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
