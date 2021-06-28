import random
count = 0
print('=-' * 21)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 21)

while True:
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ìmpar? [P/I] ')).upper()
    comput = random.randint(1, 10)
    total = valor + comput
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÌMPAR'
    print('-' * 21)
    print(f'Você jogou {valor} e o computador {comput}. Total de {total} deu {resultado}')
    print('-' * 21)
    if total % 2 == 0 and escolha == 'P' or total % 2 == 1 and escolha == 'I':
        print('Você VENCEU!')
        print('Vamos jogar novamente ...')
        count += 1
    else:
        print('Você PERDEU!')
        print('=-' * 21)
        print(f'GAME OVER! Você venceu {count} vezes.')
        break



