# coding utf=8
# Calculando o IMC

print('=' * 20)
peso = float(input('\33[32mInforme o peso:\33[m '))
altura = float(input('\33[32mInforme a altura:\33[m '))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('\33[36mVocê está Abaixo do peso!\33[m')
elif 18.5 <= imc < 25:
    print('\33[36mVocê está com o Peso ideal!\33[m')
elif 25 <= imc < 30:
    print('\33[36mVocê está em Sobrepeso!\33[m')
elif 30 <= imc < 40:
    print('\33[36mVocê está em Obesidade!\33[m')
else:
    print('\33[36mVocê está em Obesidade morbida!\33[m')
