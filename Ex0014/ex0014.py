#utf-8
#Exercício 14 do curso em vídeo de Python

celsius = float((input('Informe a temperatura em °C: ')))

#transformando de celsius para fahrenheit
fahr = (celsius * 9/5) + 32

print('A temperatura de {}°C corresponde a {}°F!'.format(celsius, fahr))
