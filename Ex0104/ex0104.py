# utf-8
# exercício 104

print('-=' * 24)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor


# Código principal
resp = leiaint('Digite um número: ')
print(f'Vocẽ acabou de digitar o número {resp}.')


