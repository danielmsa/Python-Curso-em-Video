nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minuscula é {}.'.format(nome.lower()))
print('Seu nome ao todo tem {} letras.'.format(len(nome) - nome.count(' ')))
#dividido = nome.split()
#print('Seu primeiro nome tem {} letras.'.format(len(dividido[0])))
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
