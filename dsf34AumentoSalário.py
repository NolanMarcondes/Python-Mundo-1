a = float
Sal = float(input('Qual o salário do funcionário?'))
if Sal <= 1250.00:
    a = Sal * 1.15
else:
    a = Sal * 1.10
print('O salário antigo era de {} e o novo salário é de {:.2f}'.format(Sal, a))
