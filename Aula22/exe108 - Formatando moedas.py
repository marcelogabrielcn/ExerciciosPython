import moeda

num = float(input('Informe um valor: '))
print(f'A metade desse valor é: {moeda.moeda(moeda.metade(num))}')
print(f'O dobro desse valor é: {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando o valor em 10% temos: {moeda.moeda(moeda.aumentar(num))}')
print(f'Diminuindo o valor em 10% temos: {moeda.moeda(moeda.diminuir(num))}')
