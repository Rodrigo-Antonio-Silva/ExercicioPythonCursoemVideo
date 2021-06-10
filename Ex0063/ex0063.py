#utf-8
#Sequencia de Fibonacci

term = int(input('Quantos termos da sequência Fibonacci deseja ver: '))
zero = 0
one = 1
j= 0
fi = []
fi.append(zero)
fi.append(one)
while j < (term - 2):
    sum = fi[zero] + fi[one]
    fi.append(sum)
    zero += 1
    one += 1
    j += 1
z = 0
for i in fi:
    print(i, end='')
    print(end=' → ' if z < len(fi) else print(end=' FIM'))
    z += 1
print('FIM')