vel = float(input('Qual a velocidade do carro?'))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80KM/h')
    multa = (vel-80) * 7
    print('O valor da multa é de {:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
