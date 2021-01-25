print('Gerador de PA')
print('-=-' * 10)
primeiro = int(input('Qual o primeiro termo da PA? '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Você quer ver mais quantos termos?  >'))
print('Progressão finalizada com {} termos'.format(total))
