from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5 e você terá que adivinhar...')
print('-=-'*20)
n = int(input('Digite qual o número que eu estou pensando:'))
print('Processando...')
sleep(2)
if n == computador:
    print('Parabéns! você acertou o número que eu estava pensando.')
else:
    print('Você errou! eu não estou pensando em {} e sim em {}!'.format(n,computador))
