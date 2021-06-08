a = float(input('Insira altura: '))
l = float(input('Insira Largura: '))
m2 = a * l
t = m2 / 2
#print('A parede tem {}m² e nescessita de {}litros de tinta.'.format(m2, t))
print('Sua parede tem a dimensão de {}x{} e uma área de {}m².'.format(a, l, m2))
print('Para pintar sua parede, você precisará de {}l de tinta.'.format(t))
