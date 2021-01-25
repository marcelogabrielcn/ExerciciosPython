from random import randint

print('-' * 40)
print('Olá, vamos brincar de PAR ou ÍMPAR.')
print('Será que consegue me vencer?...')
print('-' * 40)
vencedor = True
cont = 0

while vencedor:
    jogadapc = randint(0, 10)

    parouimp = str(input('Quer par ou ímpar? (P/I) ')).strip().upper()
    jogadauser = int(input('Jogue um número: '))

    tot = jogadapc + jogadauser
    if tot % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'

    if (parouimp == 'P' and resultado == 'PAR') or (parouimp == 'I' and resultado == 'ÍMPAR'):
        vencedor = True
        cont += 1
        print(f'Parabéns, você ganhou {cont} vez(es). Vamos de novo!')
    else:
        vencedor = False
    print(f'\nEu joguei {jogadapc} e você jogou {jogadauser}, {tot} é {resultado}')

print('HAHA, eu ganhei, foi bom jogar com você.')
