# utf-8
# Exercício 71

print('=' * 40)
print('{: ^40}'.format('BANCO FOGÃO'))
print('=' * 40)

count50 = count20 = count10 = countUn = 0
valor = int(input('Que valor voce quer sacar? R$ '))
while True:
    while valor >= 50:
        valor -= 50
        count50 += 1
        if valor < 50:
            break
    while valor >= 20:
        valor -= 20
        count20 += 1
        if valor < 20:
            break
    while valor >= 10:
        valor -= 10
        count10 += 1
        if valor < 10:
            break
    while valor >= 1:
        valor -= 1
        countUn += 1
        if valor == 1:
            break
    if count50 != 0:
        print(f'Total de {count50} células de R$50')
    if count20 != 0:
        print(f'Total de {count20} células de R$20')
    if count10 != 0:
        print(f'Total de {count10} células de R$10')
    if countUn != 0:
        print(f'Total de {countUn + valor} células de R$1')
    print('=' * 40)
    print('Volte sempre ao Banco Fogão! Tenha um bom dia!')
    break
