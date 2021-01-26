import random
nomes = ['a', 'b', 'c', 'd']
nomes[0] = input('Digite o 1º nome: ')
nomes[1] = input('Digite o 2º nome: ')
nomes[2] = input('Digite o 3º nome: ')
nomes[3] = input('Digite o 4º nome: ')
escolha = random.choice(nomes)
print(nomes)
print('O ganhador foi: {}'.format(escolha))
