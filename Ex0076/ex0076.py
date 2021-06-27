#utf-8
# exercicio 76

itens =('lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
        'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'livros', 34.90)
r = 'R$'
print('-=' * 22)
print('{: ^40}'.format('LISTAGEM DE PREÇOS'))
print('-=' * 22)
for pos, item in enumerate(itens):
    if pos % 2 == 0:
        print('item{:.<30}R${:>7.2f}'.format(item, itens[pos + 1]))
print('-=' * 22)

