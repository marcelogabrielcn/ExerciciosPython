from time import sleep
from random import randint

ltemp = []  # Lista temporária para adicionar a lista principal
palpites = []
cont = 1

print('-=-' * 10)
logo = 'PALPITES DA MEGA SENA'
print(f'{logo:^30}')
print('-=-' * 10)
jogos = int(input('Quantos palpites quer receber? '))
for p in range(0, jogos):
    while len(ltemp) < 6:
        num = randint(0, 60)
        if num not in ltemp:
            ltemp.append(num)
    ltemp.sort()
    palpites.append(ltemp[:])
    ltemp.clear()
for pa in palpites:
    sleep(0.5)
    print(f'Jogo {cont}: {pa}')
    sleep(0.5)
    cont += 1
print('-=-' * 10)
print('Boa sorte!!!')
