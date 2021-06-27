# utf-8
#exercício 72
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    while n > 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {extenso[n]}.')
    seguir = str(input('Deseja continuar [S/N]: ').upper().strip()[0])
    if seguir != 'S':
        break