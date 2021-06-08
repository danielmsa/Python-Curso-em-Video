p = float(input('Insira o preço: R$'))
#pd = p * 0.95
pd = p - (p * 5 / 100)
print('O preço do produto é R${} com 5% de desconto.'.format(pd))
