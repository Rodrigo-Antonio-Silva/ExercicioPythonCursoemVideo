#utf-8
soma = 0
cont =0
for i in range(1, 7):
    n = int(input('Digite o {} número: '.format(i)))
    if n % 2 == 0:
            soma += n
            cont += 1
if cont == 1:
    print('Você informou {} número par que é o :{} '.format(cont, soma))
else:
    print('Você informou {} pares e a soma dos números é :{} '.format(cont, soma))


