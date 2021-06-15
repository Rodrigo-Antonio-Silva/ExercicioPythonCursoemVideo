# utf-8
# exercício 0077
lista = []
n = 0
print('\n')
vogal = 'a', 'e', 'i', 'o', 'u'
word = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programar', 'futuro'
while n < len(word):
    for letra in word[n]:
        if letra in vogal:
            lista.append(letra)
    print(f'Na palavra {word[n].upper()} temos {" ".join(lista)}')
    n += 1
    lista.clear()
