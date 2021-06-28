from math import hypot
co = float(input('\33[32mCateto oposto:\33[m '))
ca = float(input('\33[32mCateto adjacente:\33[m '))
print('\33[35mSendo o cateto oposto {:.2f}, sendo o cateto adjacente {:.2f} a hipotenusa será: {:.2f}.\33[m'.format(co, ca, hypot(co, ca)))

"""co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)


print("Sendo o cateto oposto {}, sendo o cateto adjacente {} a hipotenusa será {:.2f}".format(co, ca, h))"""

