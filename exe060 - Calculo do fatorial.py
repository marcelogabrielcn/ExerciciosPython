num = int(input('Digite um número para descobrir seu fatorial: '))
fatorial = 1
cont = 1
while cont <= num:
   fatorial = fatorial * cont
   cont += 1
print('O fatorial de {} é {}'.format(num, fatorial))
