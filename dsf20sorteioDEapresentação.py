import random
A = str(input('Primeiro Aluno:'))
B = str(input('Segundo Aluno:'))
C = str(input('Terceiro Aluno:'))
D = str(input('Quarto Aluno:'))
lista = [A, B, C, D]
random.shuffle(lista)
print('A ordem dos escolhidos foi:')
print(lista)
