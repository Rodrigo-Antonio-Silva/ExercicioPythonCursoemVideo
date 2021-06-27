# UTF-8
# Exercício 66
count = soma = 0
while True:
        n = int(input('Digite um valor [999 para parar]: '))
        if n != 999:
                count += 1
                soma += n
        else:
                print(f'A soma dos {count} valores foi {soma}!')
                break
