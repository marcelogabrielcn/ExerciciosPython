print("Vamos somar vários valores")
num = int(input('Digite um número '))
soma = num
cont = 0
while num != 999:
    num = int(input('Digite mais um número: '))
    soma += num
    cont += 1
    print('Para sair, digite 999')
print('Voce digitou {} valores, a soma entre eles vale {} '.format(cont, soma - 999))
