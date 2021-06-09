#utf-8

while True:
    sex = str(input('Informe o Sexo [M/F]: ')).upper()
    if sex != 'M' and sex != 'F':
        print('Dados inválidos. ')
    else:
        if sex == 'M':
            print('Masculino')
        else:
            print('Feminino')
        break