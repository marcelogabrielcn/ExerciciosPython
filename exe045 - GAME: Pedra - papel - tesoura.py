from random import randint
from time import sleep
print('-=-' * 9)
print('JOGO: Pedra, Papel, Tesoura')
print('-=-' * 9)
jogadapc = randint(0, 2)
if jogadapc == 0:
    jogadapc = 'Pedra'
elif jogadapc == 1:
    jogadapc = 'Papel'
elif jogadapc == 2:
    jogadapc = 'Tesoura'
jogadauser = int(input('''Vamos jogar... Faça sua jogada: 
[1] - Pedra
[2] - Papel
[3] - Tesoura
Qual sua jogada? >>> '''))
if jogadauser == 1:
    jogadauser = 'Pedra'
elif jogadauser == 2:
    jogadauser = 'Papel'
elif jogadauser == 3:
    jogadauser = 'Tesoura'
print('\nJo')
sleep(0.5)
print('ken')
sleep(0.5)
print('po!!!')
print(f"\nEu escolho {jogadapc}, você escolheu {jogadauser}")
if (jogadapc == 'Pedra' and jogadauser == 'Tesoura') \
        or (jogadapc == 'Papel' and jogadauser == 'Pedra') \
        or (jogadapc == 'Tesoura' and jogadauser == 'Papel'):
    print('Você perdeu! HAHAHA')
elif jogadapc == jogadauser:
    print('Empate! Vamos de novo.')
else:
    print('Poxa... eu perdi. Parabéns!')
