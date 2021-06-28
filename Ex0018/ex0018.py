import math
a = float(input('\33[7;4;30mInsira um angulo:\33[m '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('\33[31mO Seno de {} é: {:.2f}\33[m\n\33[32mO coseno de {} é : {:.2f}\33[m\n\33[34mA tangente de {} é: {:.2f}\33[m'.format(a, s, a, c, a, t))
print('=' * 32)
print('Fim!!!!')
print('=' * 32)