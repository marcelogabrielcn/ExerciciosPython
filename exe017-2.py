co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = ((co ** 2) + (ca ** 2)) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
