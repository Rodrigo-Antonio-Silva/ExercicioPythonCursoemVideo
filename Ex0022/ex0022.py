n = str(input('Digite seu nome completo: ')).strip()
print('\33[31mAnalisando o seu nome...\33[m')
print('\33[35mSeu nome em maiúsculas é {}\33[m'.format(n.upper()))
print('\33[34mSeu nome em minúsculas é {}\33[m'.format(n.lower()))
print('\33[33mSeu nome tem ao todo {} letras\33[m'.format(len(n) - (n.count(' '))))
s = n.split()
print('\33[4;36mSeu primeiro nome é {} e ele tem {} letras.\33[m'.format(s[0], len(s[0])))

