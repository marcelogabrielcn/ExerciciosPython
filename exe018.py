import math
ang = int(input('Digite um ângulo: '))
num = math.radians(ang)
sen = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)
print('Seno = {:.2f}'
      '\nCos = {:.2f}'
      '\nTg = {:.2f}'.format(sen, cos, tan))
