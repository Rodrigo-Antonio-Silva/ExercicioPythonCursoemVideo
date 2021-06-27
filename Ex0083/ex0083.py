# utf-8
# exercício 83
n = 0
lista = list()
expresao = str(input('Digite a expressão: '))
for i in expresao:
    lista.append(expresao[n])
    n += 1

if '(' in lista:
    x = lista.count('(')
if ')' in lista:
    y = lista.count(')')
if x != y:
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')


