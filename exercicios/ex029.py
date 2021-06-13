vel = float(input('Qual a velocidade do carro? '))
#if vel <= 80:
#    print('Você está dentro do limite permitido.'.format(vel))
#else:
#    print('VOCÊ FOI MULTADO!')
#    print('Sua multa é de R${:.2f}, por ultrapassar o limite de velocidade permitido!'.format((vel - 80) * 7))
if vel > 80:
    print('MULTADO! Você excedeu o limite de velocidade!')
    multa = (vel - 80) * 7
    print('Você deve pagar uma multa de R$ {:.2f}!'.format(multa))
print('Tenha um bom dia. Dirija com segurança!')

