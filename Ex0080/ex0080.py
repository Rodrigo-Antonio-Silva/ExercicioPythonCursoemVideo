# utf-8
# exercício 80
num = list()
n = 0

while n <= 4:
    valor = int(input('Digite um valor: '))
    if len(num) == 0:
        print('Adicionado ao final da lista...')
        num.append(valor)
    elif valor < num[0]:
        print('Adicionado na posição 0 da lista...')
        num.insert(0, valor)
    elif valor > max(num):
        print('Adicionado ao final da lista...')
        num.append(valor)
    elif valor > num[0] and valor < num[1]:
        print('Adicionado na posição 1...')
        num.insert(1, valor)
    elif valor > num[1] and valor < num[2]:
        print('Adicionado na posição 2 da lista...')
        num.insert(2, valor)
    n += 1
print('-=' * 27)
print(f'Os valores digitados um ordem foram {num}')

