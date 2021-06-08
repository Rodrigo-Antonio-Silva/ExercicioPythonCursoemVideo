#utf-8
#Sequencia de Fibonati
n = int(input('Insira um nº: '))
f = 0
i = 0
while i < n:
    if f > 3:
        print(f-2)
    else:
        print(f)
    f += f
    f+= 1
    i+= 1
