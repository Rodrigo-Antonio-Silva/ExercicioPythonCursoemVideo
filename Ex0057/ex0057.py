#utf-8

while True:
    sex = str(input('Informe o Sexo [M/F]: ')).upper()
    if sex != 'M' and sex != 'F':
        print('Dados inválidos. ')
    else:
        if sex == 'M':
            print('Sexo Masculino registrado com sucesso.')
        else:
            print('Sexo Feminino registrado com sucesso.')
        break