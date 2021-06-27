n = float(input('A distância em metros: '))
km = n / 1000
hm = n / 100
da = n / 10
d = n * 10
c = n * 100
m = n * 1000
print('\33[31mA medida de {} metros corresponde a\33[m:\33[4;33m\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{:.0f}dm\n{:.0f}cm\n{:.0f}mm\33[m'.format(n, km, hm, da, d, c, m))

