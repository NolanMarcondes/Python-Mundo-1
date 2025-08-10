from math import hypot
ca = float(input('Qual o valor do cateto adjacente?'))
co = float(input('Qual o valor do cateto oposto?'))
hi = hypot(co, ca)
print('A hipotenusa é {}'.format(hi))
