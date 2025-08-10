from math import radians, sin, cos, tan
ang = float(input('Qual o ângulo que você deseja?'))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno de {:.2f} é {:.2f}'.format(ang, sen))
print('O cosseno de {:.2f} é {:.2f}'.format(ang, cos))
print('A tangente de {:.2f} é {:.2f}'.format(ang, tan))
