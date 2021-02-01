from random import randint

a = int(' {}'.format(randint(0, 10)))
b = int(' {}'.format(randint(0, 10)))
c = int(' {}'.format(randint(0, 10)))
d = int(' {}'.format(randint(0, 10)))
e = int(' {}'.format(randint(0, 10)))
f = (f'{a}', f'{b}', f'{c}', f'{d}', f'{e}')

print(f'Os números sorteados foram: {f}')
print(f'O menor valor foi {min(f)}')
print(f'O maior valor foi {max(f)}')
