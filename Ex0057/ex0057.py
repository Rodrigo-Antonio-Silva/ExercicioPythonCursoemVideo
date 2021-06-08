sex = str(input('Qual o sexo [M/F]:').upper().strip())
while sex not in 'MmFf':
    sex = str(input('Dados inválidos. Por favor, digite novamente:' ).upper().strip())
print(sex)