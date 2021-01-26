from random import randint
from time import sleep #tempo de espera para processar, forma animada
sort = randint(0, 5) #computafor "pensando" em um número
print("""Estou pensando em um número de 0 a 5.....
Consegue advinhar???""")
num = int(input('Digite um número >>> ')) #jogador tenta advinhar
print('Processando.....')
sleep(1)
if num == sort:
    print('Parabéns, você acertou o número que pensei.')
else:
    print('Puxa... você errou. kkkk')
print('O número que pensei era {}... você digitou {}'.format(sort, num))
