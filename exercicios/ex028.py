from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computados pensar
print('-*-' * 20)
print('Vou pensar em um número de 0 à 5. Tente advinhar...')
print('-*-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSENDO...')
sleep(2)
if jogador == computador:
    print('Ah, mizeravi! Quem te ensinou?')
else:
    print('Erooou... Eu pensei no número {}, não no {}!'.format(computador, jogador))

