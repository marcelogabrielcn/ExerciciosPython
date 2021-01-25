print('Vamos ver quantos já são maior de idade.')
maior = 0
menor = 0
for c in range(1, 8):
    idade = int(input('Digite a idade da {}º pessoa: '.format(c)))
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Deste grupo, {} são maiores de idade, os outros {} ainda não.'.format(maior, menor))
