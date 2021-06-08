from random import randint
from time import sleep
n = randint(0, 5) # Faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número tente adinvinhar....')
print('-=-' * 20)
u = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar.
print('processando.....')
sleep(2)
if n == u:
    print('Parabéns! Você consegui me vencer!') # Jogador adivinhou
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(n, u)) # Jogador não acertou


