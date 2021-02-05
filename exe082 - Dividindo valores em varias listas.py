lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    if continuar == 'N':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
pares.sort()
impares.sort()
print('-=-' * 20)
print(f'\nA lista completa ficou assim {lista}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores ímpares foram: {impares}')
