from time import sleep

print('-' * 30)
print('{:^30}'.format('BANCO MARQUES DIGITAL'))
print('-' * 30)
print('\nOlá, seja bem-vindo ao banco Marques Digital.\n')
completename = str(input('Digite seu nome completo: ')).strip().split()
name = completename[0]
saldo = 10000
not50 = not20 = not10 = not5 = not2 = moe1 = 0
continuar = 'S'

print(f'Muito bem {name}, você possui um saldo de R${saldo:.2f}')
print('\nTemos apenas cédulas no valor de R$50,00 R$20,00 R$10,00 R$5,00 R$2,00 e moeda de R$1,00')

while continuar != 'N' and saldo > 0:
    saque = int(input('Qual valor deseja retirar de sua conta? >>> R$'))
    while saque > saldo:
        print('Ops, você não possui o valor que deseja sacar.')
        saque = int(input('\nQual valor deseja retirar de sua conta? >>> R$'))

    while saque <= 0:
        print('Oops, não pode sacar valor negativo ou nulo haha.')
        saque = int(input('Qual valor deseja retirar de sua conta? >>> R$'))

    saldo -= saque

    if saque >= 50:
        not50 = int(saque / 50)
        saque -= not50 * 50
    if saque >= 20:
        not20 = int(saque / 20)
        saque -= not20 * 20
    if saque >= 10:
        not10 = int(saque / 10)
        saque -= not10 * 10
    if saque >= 5:
        not5 = int(saque / 5)
        saque -= not5 * 5
    if saque >= 2:
        not2 = int(saque / 2)
        saque -= not2 * 2
    if saque >= 1:
        moe1 = int(saque / 1)
        saque -= moe1 * 1
    print('Contando as cédulas...')
    sleep(3)
    print('\nPronto! Retire o valor abaixo.')
    print('-' * 20)
    print(f'''    {not50} notas de R$50,00
    {not20:3} notas de R$20,00
    {not10:3} notas de R$10,00
    {not5:3} notas de R$5,00
    {not2:3} notas de R$2,00
    {moe1:3} moeda de R$1,00''')
    print('-' * 20)
    print(f'\nVocê possui um saldo de R${saldo:.2f}')
    continuar = str(input('Deseja sacar outro valor? (S/N): ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja sacar outro valor? (S/N): ')).strip().upper()[0]
print('\nObrigado por utilizar nossos serviços, até logo.')