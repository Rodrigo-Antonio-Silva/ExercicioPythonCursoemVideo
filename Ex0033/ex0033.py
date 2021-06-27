#coding utf-8
#código para identificar o maior e o menor valor dentre três digitados pelo usuário.

n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
l = n1, n2, n3
nf = sorted(l)
print('O maior valor digitado foi: \33[36m{}\33[m.\nO menor valor digitado foi: \33[31m{}\33[m.'.format((nf[2]), (nf[0])))

