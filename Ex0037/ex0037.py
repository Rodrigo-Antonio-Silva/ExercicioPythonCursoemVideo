# coding utf-8
# exercício conversão

num = int(input('Digite um numero: '))
print('Escolha uma das bases de conversão:')
print('=' * 27)
print('[1] converter em binário.')
print('[2] converter em octal.')
print('[3] converter em hexadecimal.\n')
print('=' * 27)
escolha = int(input('Qual será a base de conversão? '))
print('-' * 27)
if escolha == 1:
    print('\33O número {} em binário seria {}.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em octal seria {}.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O numero {} em hexadecimal seria {}.'.format(num, hex(num)[2:]))
else:
    print('conversão não indicada, tente novamente.')