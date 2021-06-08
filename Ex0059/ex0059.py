n1 = int(input('Insira o 1ª número: '))
n2 = int(input('Insira o 2ª número: '))
print('-' * 36)
print('Qual opção você deseja?')
print('-' * 36)
opcao = 0
while opcao != 5:
    print('[1]\33[35msomar\33[m\n[2]\33[35mmultiplicar\33[m\n[3]\33[35mmaior\33[m'
              '\n[4]\33[35mnovos números\33[m\n[5]\33[35msair do programa\33[m')
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(n1, n2, (n1+n2)))
    elif opcao == 2:
        print('A multiplicação de {} e {} é igual a {}.'.format(n1, n2, (n1 * n2)))
    elif opcao == 3:
        if n1 > n2:
            print('O maior número é {}.'.format(n1))
        else:
            print('O maior número é {}.'.format(n2))
    elif opcao == 4:
        n1 = int(input('Insira um novo número: '))
        n2 = int(input('Insira um novo número: '))
    else:
        print('\nVoce saiu do programa! Até logo!!')
