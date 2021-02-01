numeros = (int(input('Digite um valor: ')),
           int(input('Digite outro valor: ')),
           int(input('Digite mais um valor: ')),
           int(input('Digite o último valor: ')))

print(f'\nOs números digitados foram: {numeros[0]} {numeros[1]} {numeros[2]} {numeros[3]}')
print(f'O número 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O número 3 aparece em {numeros.index(3) + 1}º lugar')
else:
    print('O número 3 não aparece nessa tupla')
print('Os valores pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'{n} ', end='')
