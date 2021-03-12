dici = {}
gols = []
tot = 0

dici['nome'] = str(input('Digite o nome do jogador: '))
dici['partidas'] = int(input(f'Quantas partidas {dici["nome"]} jogou essa temporada? '))
for g in range(0, dici["partidas"]):
    gols.append(int(input(f'Quantos gols o jogador fez no jogo {g+1}? ')))
    dici['gols'] = gols
for gol in gols:
    tot += gol
dici['total'] = tot
print('-=-' * 10)
print(dici)
print('-=-' * 10)
for k, v in dici.items():
    print(f'O campo {k} tem valor {v}')
print('-=-' * 10)
print(f'O jogador {dici["nome"]} jogou ao todo {dici["partidas"]} partidas')
for i, v in enumerate(gols):
    print(f'   => No jogo {i+1} fez {v} gols')
print('fim')
