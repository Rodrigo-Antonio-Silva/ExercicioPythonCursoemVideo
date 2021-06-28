# utf-8
# exercício 78

lista = list()
listaMax = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite um valor para posição {i}: ')))
print('-=' * 21)
print(f'Você digitou os valores {lista}.')
n = 0
m = 0
print(f'O maior valor digitado foi {max(lista)} na posição: ', end='')
for pos, item in enumerate(lista):
    if max(lista) == lista[n]:
        print(pos, end='...')
    n += 1
print(f'\nO menor valor digitado foi {min(lista)} na posição: ', end='')
for pos, item in enumerate(lista):
    if min(lista) == lista[m]:
        print(pos, end='...')
    m += 1

