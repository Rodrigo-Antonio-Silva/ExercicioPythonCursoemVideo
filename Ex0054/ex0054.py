#utf-8
from datetime import date
l = []
atual = date.today().year
for i in range(1, 8):
    n = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    l.append(atual - n)
print('Ao todo {} pessoas atingiram a maioridade.'.format(len((list(filter(lambda x: x >= 21, l))))))
print('Ao todo {} pessoas não atingiram a maioridade.'.format(len(list(filter(lambda x: x < 21, l)))))