print('Vamos somar os números ímpares, divisiveis por 3, entre 0 e 500')
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('Ao todo foram {} números ímpares, divisieveis por três entre 0 e 500.\n'
      'A soma entre eles dá {}'.format(cont, soma))
