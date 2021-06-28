from random import shuffle
p = input('Primeiro Aluno: ')
s = input('Segundo Aluno: ')
t = input('Terceiro Aluno: ')
q = input('Quarto Aluno: ')
lista = [p, s, t, q]
shuffle(lista)
print('A ordem de apresentação será: ')
print('\33[31m{}\33[m'.format(lista))





