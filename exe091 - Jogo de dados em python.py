from random import randint
from time import sleep

jogadores = dict()
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
print('VALORES SORTEADOS')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v}')
    sleep(0.5)
print('-=-' * 10)
print('RANKING DOS JOGADORES')

print('Fim do Programa')
