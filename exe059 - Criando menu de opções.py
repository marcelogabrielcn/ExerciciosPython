num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
print('\nVocê digitou {} e {}. O que deseja fazer com esses valores?'.format(num1, num2))
escolha = int(input("""\n[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Inserir outros valores
[5] - Sair do programa
>>> """))
print(escolha)
while escolha != 5:
    if escolha == 1:
        print('A soma entre {} e {} é {}'.format(num1, num2, (num1 + num2)))
    elif escolha == 2:
        print('A multiplicação entre {} e {} é {}'.format(num1, num2, (num1 * num2)))
    elif escolha == 3:
        if num1 > num2:
            print('O número {} é maior do que {}'.format(num1, num2))
        else:
            print('O número {} é maior do que {}'.format(num2, num1))
    elif escolha == 4:
        print('Ok, vamos redefinir os valores!')
        num1 = int(input('Digite um número: '))
        num2 = int(input('Digite outro número: '))
    else:
        print('Oops, número inválido, digite outro por favor.')

    print('\nO que deseja fazer agora?')
    escolha = int(input("""\n[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Inserir outros valores
[5] - Sair do programa
>>> """))
