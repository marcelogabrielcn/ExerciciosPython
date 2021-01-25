n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('O aluno teve média {}, esta REPROVADO'.format(m))
elif m <= 6.9:
    print('O aluno teve média {}, esta de RECUPERAÇÃO'.format(m))
else:
    print('O aluno teve média {}, esta APROVADO'.format(m))
print('Continuem estudando.')
