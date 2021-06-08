n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print('=' * 28)
mean = (n1 + n2) / 2
if mean < 5.0:
    print('\nO aluno foi REPROVADO')
elif 5.0 <= mean < 7.0:
    print('\nO aluno está em RECUPERAÇÃO')
else:
    print('\nO aluno está Aprovado')
print('-' * 28)
print('A média do aluno foi de {:.2f}'.format(mean))


