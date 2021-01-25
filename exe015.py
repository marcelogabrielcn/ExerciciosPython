dias = int(input('Por quantos dias o carro foi alugado? :'))
km = float(input('Quantos Quilometros o carro percorreu? :'))
valor = (dias * 60) + (km * 0.15)
print('O valor total do aluguel é de R${:.2f}'.format(valor))
