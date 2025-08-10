a = float(input('Primeiro seguimento:'))
b = float(input('Segundo seguimento:'))
c = float(input('Terceiro seguimento:'))
if a < (b + c) and b < (a + c) and c < (a + b):
    print('Os seguimentos podem formar um triângulo')
else:
    print('Os seguimentos não podem formar um triângulo')
