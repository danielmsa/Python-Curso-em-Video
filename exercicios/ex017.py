#import math
from math import hypot
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
#hi = (cato ** 2 + cata ** 2) ** (1/2)
#hi = math.hypot(cato, cata)
#print('A hipotenusa vai medir {:.2f}.'.format(hi))
print('A hipotenusa vai medir {:.2f}.'.format(hypot(cato, cata)))

