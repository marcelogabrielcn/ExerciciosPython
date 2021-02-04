lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'\nForam digitados ao todo {len(lista)} valores.')
lista.sort(reverse=True)
print(f'A lista decrescente fica desta forma: {lista}')
if 5 in lista:
    print(f'O valor 5 aparece {lista.count(5)} vezes na lista')
else:
    print('O valor 5 não foi encontrado na lista')
