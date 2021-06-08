#utf-8
#Exercício 15 do curso de python do Curso em Vídeo

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))

diaria = 60
consumo = 0.15

#cálculo do total a pagar
totaldias = dias * diaria
totalkm = km * consumo

print('O total a pagar é de R${:.2f}'.format(totaldias + totalkm))

