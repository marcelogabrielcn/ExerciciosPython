from random import randint

maiorvalor = 0
menorvalor = 0

a = ' {}'.format(randint(0, 9))
b = ' {}'.format(randint(0, 9))
c = ' {}'.format(randint(0, 9))
d = ' {}'.format(randint(0, 9))
e = ' {}'.format(randint(0, 9))
f = (f'{a}', f'{b}', f'{c}', f'{d}', f'{e}')
print(f)
print(type(f))
