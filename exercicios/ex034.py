sal = float(input('Qual o salário do funcionário? R$  '))
if sal <= 1250:
    dis = sal * 1.15
else:
    dis = sal * 1.10
print('O salario do funcionário era R${:.2f} e passará a ser R${:.2f}.'.format(sal, dis))
