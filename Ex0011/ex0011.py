l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m = l * a
t = m / 2
print('\33[4;33mSua parede tem a dimensão de {} X {} e sua área é de {}m2.\33[m'.format(l, a, m))
print('\33[4;33mPara pintar essa parade, você precisará de {} l de tinta.\33[m'.format(t))

