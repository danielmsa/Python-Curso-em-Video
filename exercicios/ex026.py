f = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes.'.format(f.count('A')))
print('Ela aperece pela primeira vez na posição {}'.format(f.find('A')))
print('Ela aparece pela ultima vez na posição {}.'.format(f.rfind('A')+1))


