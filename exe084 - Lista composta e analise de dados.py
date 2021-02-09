lista = ltemp = []
maispeso = menospeso = 0
while True:
    ltemp = [str(input('Digite o nome do participante: ')), int(input('Digite o peso do participante: '))]
    lista.append(ltemp[:])
    if maispeso == 0:
        maispeso = ltemp[1]
        menospeso = ltemp[1]
    elif ltemp[1] > maispeso:
        maispeso = ltemp[1]
    elif ltemp[1] < menospeso:
        menospeso = ltemp[1]
    ltemp.clear()
    continuar = str(input('Quer cadastrar outro participante? (S/N) ')).strip()[0].upper()
    while continuar not in 'NS':
        continuar = str(input('Quer cadastrar outro participante? (S/N) ')).strip()[0].upper()
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'Ao todo foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maispeso}Kg. Peso de ', end='')
for i, v in enumerate(lista):  # i é o índice, v é o valor
    for n, p in enumerate(v):  # n é o nome, p é o peso
        if p == maispeso:
            print(v[0], end=', ')
print(f'\nO menor peso foi de {menospeso}Kg. Peso de ', end='')
for i, v in enumerate(lista):
    for n, p in enumerate(v):
        if p == menospeso:
            print(v[0], end=', ')
print('\nFIM')
