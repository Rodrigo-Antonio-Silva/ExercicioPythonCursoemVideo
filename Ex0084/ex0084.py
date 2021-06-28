# utf-8
# exercício 84

pessoas = list()
cadastro = list()
peso = list()
nome = list()
n = m = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    cadastro.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if resp != 'S':
        break
print('-=' * 30)
for p in cadastro:
    nome.append(p[0])
    peso.append(p[1])
print(f'Ao todo, você cadastrou {len(cadastro)}.')
print(f'O maior peso foi de {max(peso):.2f} kg. Peso de ', end='')
for x in peso:
    if max(peso) == peso[n]:
        print(nome[n].split(), end=' ')
    n += 1
print(f'\nO menor peso foi de {min(peso):.2f} kg. Peso de ', end='')
for y in peso:
    if min(peso) == peso[m]:
        print(nome[m].split(), end=' ')
    m += 1