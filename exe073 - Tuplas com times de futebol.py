print('Olá, veja a seguir a lista dos colocados do Brasileirão - Série A')
brasileirao = ('Internacional', 'São Paulo', 'Flamengo', 'Atlético-MG', 'Palmeiras', 'Grêmio',
               'Fluminense', 'Corinthians', 'Santos', 'Ceará', 'Bragantino', 'Athletico-PR',
               'Atlétoco-GO', 'Fortaleza', 'Bahia', 'Sport Recife', 'Vasco da Gama', 'Coritiba', 'Goiás', 'Botafogo')
print('-=-' * 25)
cont = 1
for c in brasileirao:
    print(f'{cont:2}º - {brasileirao[cont - 1]}')
    cont += 1
print('-=-' * 25)
print('\nAgora veja os cinco primeiros colocados')
print(brasileirao[0:5])
print('-=-' * 25)
print('\nAgora veja os que serão rebaixados')
print(brasileirao[-5:])
print('-=-' * 25)
print('\nVeja a lista em ordem alfabetica')
print(sorted(brasileirao))
print('-=-' * 25)
meutime = str(input('Digite o nome do seu time e veja sua posição, digite corretamente: '))
print(f'\nO {meutime} está em {brasileirao.index(meutime) + 1}º colocado')
