from random import randint
from time import sleep  # tempo de espera para processar, forma animada

sort = randint(0, 10)  # computafor "pensando" em um número
cont = 1
print("""Estou pensando em um número de 0 a 10.....
Consegue advinhar???""")
num = int(input('Digite um número >>> '))  # jogador tenta advinhar
print('Processando.....')
sleep(1)
if num == sort:
    print('Parabéns, você acertou de primeira o número que pensei.')
else:
    print('Puxa... você errou. kkkk. Tente novamente')
    while num != sort:
        if num < sort:
            print('Mais...')
        else:
            print('Menos...')
        num = int(input('Digite um número >>> '))  # jogador tenta advinhar
        cont += 1
print('O número que pensei era {}... você digitou {}'.format(sort, num))
print('Você acertou em {} jogadas.'.format(cont))
