d = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {:.1f} KM.'.format(d))
if d <= 200:
    print('E preço da passagem será de R$ {:.2f}'.format(d * 0.50))
else:
    print('E o preço da passagem será de R$ {:.2f}'.format(d * 0.45))

