preco = float(input('Qual o preço do produto?'))
desc = preco-(preco*5/100)
print('O produto de R${:.2f} sairá por R${:.2f} com desconto de 5%'.format(preco, desc))
