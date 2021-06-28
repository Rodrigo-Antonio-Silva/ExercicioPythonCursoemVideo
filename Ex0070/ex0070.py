#utf-8
#Exercício 70

print('-' * 30)
print('{: ^30}'.format('SUPER FOGAO LTDA.'))
print('-' * 30)

lprod = []
lpreco =[]

while True:
    prod = str(input('Nome do Produto: '))
    lprod.append(prod)
    preco = float(input('Preço R$ '))
    lpreco.append(preco)
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        print('---------------- FIM DO PROGRAMA -------------------')
        print(f'O total da compra foi R${sum(lpreco):.2f}')
        print(f'Temos {sum(i > 1000 for i in lpreco)} produtos custando mais de R$1000.00.')
        print(f'O produto mais barato foi {lprod[lpreco.index(min(lpreco))]} que custa R${min(lpreco):.2f}.')
        break
