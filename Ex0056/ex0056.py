from functools import reduce
nome = []
idade = []
sexo = []
for i in range(0, 2):
    nome.append(input('Nome:'))
    idade.append(input('Idade: '))
    sexo.append(input('Sexo:'))
mais_velho = (reduce((lambda x, y: x if (x > y)else y),idade))
indice_mais_velho = idade.index(mais_velho)
print('{} é a maior idade.'.format(mais_velho))
print('A pessoa com mais idade se chama {}.'.format(nome[indice_mais_velho]))

