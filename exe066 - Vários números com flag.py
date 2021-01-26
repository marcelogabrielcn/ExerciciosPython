num = int(input('Digite um número (999 para parar): '))
soma = num
cont = 1
while num != 999:
    num = int(input('Digite um número (999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'A soma dos {cont} números é igual a {soma}.')
