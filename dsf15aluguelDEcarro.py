D = int(input('Quantos dias o carro ficou alugado?'))
K = float(input('Quantos Km o carro rodou?'))
D1 = 60*D
K1 = 0.15*K
print('O preço  a ser pago por dia é de R${:.2f} e por Km rodado é de R${:.2f} totalizando:R${:.2f}'.format(D1, K1, D1+K1))
