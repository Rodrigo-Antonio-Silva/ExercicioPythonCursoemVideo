# coding utf-8
# Pedra, papel e tesoura

import random
from time import sleep
print('''Opções:
[0] pedra
[1] papel
[2] tesoura''')
r = [0, 1, 2]

m = random.randint(0, 2)
eu = int(input('\33[32mQual a sua escolha:\33[m '))
print('PEDRA')
sleep(1.3)
print('PAPEL')
sleep(1.3)
print('TESOURA!!!!')
sleep(1)
print('=' * 24)
if eu in r:
    if eu == 0:
        print('\33[36mVocê escolheu pedra.\33[m')
    elif eu == 1:
        print('\33[36mVocê escolheu papel.\33[m')
    elif eu == 2:
        print('\33[36mVocê escolheu tesoura.\33[m')
else:
    print('\33[37mNão existe essa opção.\33[m')
if m == 0:
    print('\33[35mEu escolhi pedra.\33[m')
elif m == 1:
    print('\33[35mEu escolhi papel.\33[m')
elif m == 2:
    print('\33[35mEu escolhi tesoura.\33[m')
print('=' * 24)
if m == eu:
    print('\n\33[31mEmpatamos!\33[m')
elif m == 0 and eu == 1:
    print('\n\33[31mParabéns, você ganhou!\33[m')
elif m == 0 and eu == 2:
    print('\n\33[31mQue bom eu ganhei!\33[m')
elif m == 1 and eu == 0:
    print('\n\33[31mQue bom eu ganhei!\33[m')
elif m == 1 and eu == 2:
    print('\n\33[31mParabéns, você ganhou!\33[m')
elif m == 2 and eu == 0:
    print('\n\33[31mParabéns, você ganhou!\33[m')
elif m == 2 and eu == 1:
    print('\n\33[31mQue bom eu ganhei!\33[m')



