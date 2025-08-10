dist = float(input('Qual a distância da viagem?'))
if dist <= 200:
    valor = dist * 0.5
    print('O valor da sua passagem é de R${:.2f}'.format(valor))
else:
    valor2 = dist * 0.45
    print('O valor da sua passagem é de R${:.2f}'.format(valor2))
