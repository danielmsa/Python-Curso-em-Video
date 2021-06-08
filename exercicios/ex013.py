s = float(input('Salário: R$'))
#d = s * 1.15
d = s + (s * 15/100)
print('O salário é de R${:.2f} e passa a ser de R${:.2f} com o aumento de 15%.'.format(s, d))

