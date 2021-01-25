num = int(input('Digite um número: '))

media = 0
soma = num
cont = 0
maiornum = num
menornum = num
print('Para sair digite 999')
while num != 999:

    if num > maiornum:
        maiornum = num
    elif num < menornum:
        menornum = num
    num = int(input('Digite outro número: '))
    soma += num
    cont += 1
media = (soma - 999) / cont
print('Você digiou {} valores, a média entre eles é {}'.format(cont, media))
print('O maior número digitado foi {} e o menor foi {}'.format(maiornum, menornum))
