v = float(input('Qual é a velocidade atual do carro em KM/h? '))
if v > 80.0:
    print('Multado! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa '
          'de R$ {:.2f}!'.format((v - 80) * 7))
print('Tenha um bom dia! Dirija com segurança!')
