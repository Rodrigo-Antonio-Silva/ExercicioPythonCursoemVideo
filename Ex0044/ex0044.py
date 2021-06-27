# coding utf-8
# Calculando desconto
print('=' * 24)
# informando o valor
valor = float(input('\33[36mQual o valor do produto?: \33[m'))
print('''Forma de pagamento 
[1] à vista dnheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

# informando a condição de pagamento
cond = str(input('\33[36mQual a condição de pagamento? \33[m'))


if cond == '1':
    print('\33[36mPagamento à vista 10% de desconto, valor a pagar R$ {:.2f}.\33[m'.format(valor * 0.90))
elif cond == '2':
    print('\33[36mPagamento em uma vez no cartão 5% de desconto, valor a pagar R$ {:.2f}.\33[m'.format(valor * 0.95))
elif cond == '3':
    print('\33[36mSua compra será parcelada em 2x de R$ {:.2f}.\33[m'.format(valor/2))
    print('\33[36mSua compra vai custar R$ {:.2f} no final.'.format(valor))
elif cond == '4':
    p = int(input('Quantas parcelas?'))
    print('\33[36mSua compra será parcelada em {:.2f}x de R$ {:.2f} com juros.\33[m'.format(p, (valor/p)*1.2))
    print('\33[36mSua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(valor, (valor * 1.2)))
else:
    print('Essa condição não existe!')