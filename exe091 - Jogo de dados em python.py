from operator import itemgetter
from random import randint
from time import sleep

jogadores = dict()
ranking = []
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
print('VALORES SORTEADOS')
for k, v in jogadores.items():
    sleep(0.5)
    print(f'{k} tirou {v}')
    sleep(0.5)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-=-' * 10)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'    {i+1}º Lugar {v[0]} com {v[1]}.')
    sleep(0.5)
print('Fim do Programa')
