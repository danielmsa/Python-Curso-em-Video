from random import choice
a1 = str(input('Primeiro Aluno: '))
a2 = str(input('Segundo Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
list = [a1 , a2 , a3 , a4]
pick = choice(list)
print('O aluno escolhido foi {}.'.format(pick))






