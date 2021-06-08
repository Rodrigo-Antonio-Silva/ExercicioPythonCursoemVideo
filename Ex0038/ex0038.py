# coding utf-8
# exercício comparação entre dois números

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print('O primeiro valor {} é o maior.'.format(num1))
elif num2 > num1:
    print('O segundo valor {} é o maior.'.format(num2))
else:
    print('Não existe valor maior, {} e {} são iguais.'.format(num1, num2))
