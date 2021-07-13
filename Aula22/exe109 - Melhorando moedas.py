import moeda

num = float(input('Informe um valor: '))
print(f'A metade desse valor é: {moeda.metade(num, True)}')
print(f'O dobro desse valor é: {moeda.dobro(num, True)}')
print(f'Aumentando o valor em 10% temos: {moeda.aumentar(num)}')
print(f'Diminuindo o valor em 10% temos: {moeda.diminuir(num)}')
