velo = int(input('Digite a velocidade do carro: '))
if velo > 80:
    print('Eita, o limite de velocidade é 80Km/h.')
    multa = (velo - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
else:
    print('Muito bem, continue dentro do limite de velocidade!')
print('Tenha uma boa viagem.')
