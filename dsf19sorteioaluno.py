import random
a = str(input('Primeiro Aluno:'))
b = str(input('Segundo Aluno:'))
c = str(input('Terceiro Aluno:'))
d = str(input('Quarto Aluno:'))
lista = (a, b, c, d)
escolhido = random.choice(lista)
print('O aluno escolhido foi {}!!'.format(escolhido))
