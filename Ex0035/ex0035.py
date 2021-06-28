#coding utf-8
#código para verificar se três lados formam um triângulo.
print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
     print('\33[7;30mOs segmentos acima podem formar um triângulo!\33[m')
else:
    print('\33[7;30mOs segmentos acima não podem formar um triângulo!\33[m')
