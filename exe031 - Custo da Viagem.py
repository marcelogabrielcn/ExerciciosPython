dist = int(input('Digite a distância da viagem em KM:  '))
if dist <= 200:
    valor = dist * 0.50
    print('O valor da sua viagem será R${:.2f}'.format(valor))
else:
    valor = dist * 0.45
    print('O valor da sua viagem será R${:.2f}'.format(valor))
print('Tenha uma boa viagem.')