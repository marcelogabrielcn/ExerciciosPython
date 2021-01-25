r1 = int(input('Digite a medida da primeira reta: '))
r2 = int(input('Digite a medida da segunda reta: '))
r3 = int(input('Digite a medida da terceira reta: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Essas retas podem formar um triângulo.')
    print('\nAgora vamos analizar o tipo de triângulo.\n')
    if r1 == r2 and r2 == r3:
        print('Esses valores formam um triângulo EQUILÁTERO, pois todos os lados são iguais.')
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print('Esses valores formam um triângulo ISÓSCELES, pois temos dois lados iguais.')
    else:
        print('Esses valores formam um triângulo ESCALENO, pois todos os lados são diferentes.')
else:
    print('Essas retas não podem formar um triângulo.')

