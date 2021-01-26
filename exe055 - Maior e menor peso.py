print('Vamos ver quem é o mais pesado e o mais leve.')
maisp = 0
menosp = 0
nomemaisp = ''
nomemenosp = ''
for c in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        menosp = peso
        maisp = peso
        nomemaisp = c
        nomemenosp = c
    if peso > maisp:
        maisp = peso
        nomemaisp = c
    elif peso < menosp:
        menosp = peso
        nomemenosp = c
print('A pessoa mais pesada foi a {}ª, com {}Kg'.format(nomemaisp, maisp))
print('A pessoa mais leve foi a {}ª, com {}Kg'.format(nomemenosp, menosp))
