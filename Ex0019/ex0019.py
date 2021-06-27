from random import choice
p = input('\33[4mPrimeiro Aluno:\33[m ')
s = input('\33[4mSegundo Aluno:\33[m ')
t = input('\33[4mTerceiro Aluno:\33[m ')
q = input('\33[4mQuarto Aluno:\33[m ')
lista = [p, s, t, q]
print('O Aluno escolhido foi: {}'.format(choice(lista)))












