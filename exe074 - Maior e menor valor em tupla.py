from random import randint

maiorvalor = 0
menorvalor = 0

a = int(' {}'.format(randint(0, 9)))
if a > maiorvalor:
    maiorvalor = a
if menorvalor == 0:
    menorvalor = a
b = int(' {}'.format(randint(0, 9)))
if b > maiorvalor:
    maiorvalor = b
if b < menorvalor:
    menorvalor = b
c = int(' {}'.format(randint(0, 9)))
if c > maiorvalor:
    maiorvalor = c
if c < menorvalor:
    menorvalor = c
d = int(' {}'.format(randint(0, 9)))
if d > maiorvalor:
    maiorvalor = d
if d < menorvalor:
    menorvalor = d
e = int(' {}'.format(randint(0, 9)))
if e > maiorvalor:
    maiorvalor = e
if e < menorvalor:
    menorvalor = e
f = (f'{a}', f'{b}', f'{c}', f'{d}', f'{e}')

print(f'Os números sorteados foram: {f}')
print(f'O menor valor foi {menorvalor}')
print(f'O maior valor foi {maiorvalor}')
