d = int(input('Dias alugado: '))
k = float(input('Km rodado: '))
t = (d * 60) + (k * 0.15)
print('O total devido pelo aluguél do carro é de R${:.2f}.'.format(t))
