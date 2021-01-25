peso = float(input('Digite seu peso em Kg. '))
altura = float(input('Digite sua altura em Metros. ex.(1.85): '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    stt = 'Abaixo do Peso'  # stt = Status
elif imc <= 25:
    stt = 'Peso Ideal'
elif imc <= 30:
    stt = 'Acima do Peso'
elif imc <= 40:
    stt = 'Obesidade'
else:
    stt = 'Obesidade Mórbida'
print('Seu IMC está em {:.2f}. Status: {}!'.format(imc, stt))
