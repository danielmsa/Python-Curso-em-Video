from math import radians, sin, cos, tan
ang = float(input('Digite o Ângulo que você deseja: '))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}.'.format(ang, s))
print('O ângulo de {} tem o COSENO de {:.2f}.'.format(ang, c))
print('O ângulo de {} tem a TENGENTE de {:.2f}.'.format(ang, t))

