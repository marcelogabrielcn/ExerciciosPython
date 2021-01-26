from random import randint

a = ' {}'.format(randint(0, 9))
b = ' {}'.format(randint(0, 9))
c = ' {}'.format(randint(0, 9))
d = ' {}'.format(randint(0, 9))
e = ' {}'.format(randint(0, 9))
f = a + b + c + d + e
print(f)
print(type(f))
