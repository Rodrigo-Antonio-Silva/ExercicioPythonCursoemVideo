# utf-8
# exercicio 74
from random import randint

tupla = (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10)), (randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for i in tupla:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')




