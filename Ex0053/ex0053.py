# utf-8
#palindromo
se = []
f = str(input('Digite a frase: ').lower())
se = f.replace(' ', '').replace('.', '')
if se == se[::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo.')