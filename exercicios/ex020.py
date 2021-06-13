from random import shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
list = [a1, a2, a3, a4]
shuffle(list)
print('A ordem de apresentação será {}.'.format(list))


