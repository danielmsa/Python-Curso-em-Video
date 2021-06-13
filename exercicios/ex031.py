dist = int(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(dist))
if dist <= 200:
    price = dist * 0.50
else:
    price = dist * 0.45
#price = dist * 0.50 if dist <= 200 else dist * 0.45
print('O preço da sua passagem será de R${:.2f}.'.format(price))
