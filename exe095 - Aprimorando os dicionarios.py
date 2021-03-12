dici = {}
gols = []
tot = 0
jogadores = {}

while True:
    dici['nome'] = str(input('Digite o nome do jogador: '))
    dici['partidas'] = int(input(f'Quantas partidas {dici["nome"]} jogou essa temporada? '))
    for g in range(0, dici["partidas"]):
        gols.append(int(input(f'Quantos gols o jogador fez no jogo {g+1}? ')))
        dici['gols'] = gols
    for gol in gols:
        tot += gol
    dici['total'] = tot
    jogadores[len(jogadores)] = dici.copy()
    dici.clear()
    continuar = str(input('Quer continuar? (S/N) ')).upper()[0].strip()
    if continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).upper()[0].strip()
    if continuar == 'N':
        break

print('-=-' * 30)
print(jogadores)
print('Cod.  Nome        Gols           Total')
for i, v in enumerate(jogadores):
    print(f'{i:<6}', end='')
