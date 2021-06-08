s = float(input('Qual o salário do funcionário? R$ '))
if s > 1250.00:
    print('Quem ganhava R$ \33[33m{:.2f}\33[m, passa a ganhar R$ \33[36m{:.2f}\33[m agora.'.format(s, (s * 1.10)))
elif s <= 1250.00:
    print('Quem ganhava R$ \33[33m{:.2f}\33[m, passa a ganhar R$ \33[31m{:.2f}\33[m agora.'.format(s, (s * 1.15)))