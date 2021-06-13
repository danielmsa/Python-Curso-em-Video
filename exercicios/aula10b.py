n1 = float(input('Digite a primeira nota: '))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}.'.format(m))
if m >= 7.0:
    print('Aprovado! Não fez mais que a sua obrigação!')
else:
    print('Reprovado! Que vergonha, hein? Vai estudar vagabundo!')
