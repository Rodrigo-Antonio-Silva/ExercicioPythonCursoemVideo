# coding utf-8
# exercício 42
print('=-=' * 16)
print('======Analisador de triângulos======')
print('=-=' * 16)

r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
     print('\33[32mOs segmentos acima podem formar um triângulo!\33[m')
     if r1 == r2 == r3:
            print('\n\33[7;36mTriângulo Equilátero.\33[m')
     elif r1 != r2 != r3 != r1:
            print('\n\33[7;36mTrinângulo Escaleno.\33[m')
     else:
            print('\n\33[7;36mTriângulo Isóceles.\33[m')
else:
    print('\33[7;30mOs segmentos acima não podem formar um triângulo!\33[m')