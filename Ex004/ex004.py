n = input('Digite algo:')
print('O tipo primitivo desse valor é \33[36m{}\33[m?'.format(type(n)))
print('Só tem espaços? \33[33m{}\33[m'.format(n.isspace()))
print('É um número? \33[33m{}\33[m'.format(n.isnumeric()))
print('É alfanumérico? \33[33m{}\33[m'.format(n.isalnum()))
print('Está em maiuscúlas? \33[33m{}\33[m'.format(n.isupper()))
print('Está em minuscúlas? \33[33m{}\33[m'.format(n.islower()))
print('Está capitalizada? \33[33m{}\33[m'.format(n.istitle()))

