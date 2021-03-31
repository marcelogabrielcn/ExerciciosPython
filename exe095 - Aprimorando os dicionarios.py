dici = {}
gols = []
jogadores = []

while True:
    dici['nome'] = str(input('Digite o nome do jogador: '))
    dici['partidas'] = int(input(f'Quantas partidas {dici["nome"]} jogou essa temporada? '))
    for g in range(0, dici["partidas"]):
        gols.append(int(input(f'Quantos gols o jogador fez no jogo {g+1}? ')))
        dici['gols'] = gols.copy()
    dici['total'] = sum(gols)
    jogadores.append(dici.copy())
    dici.clear()
    gols.clear()
    continuar = str(input('Quer continuar? (S/N) ')).upper()[0].strip()
    if continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) ')).upper()[0].strip()
    if continuar == 'N':
        break

print('-=-' * 30)
print('Cod.  Nome        Partidas          Gols           Total')
for k, v in enumerate(jogadores):
    print(f'{k:<6}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-=-' * 30)
while True:
    pesquisa = int(input('Quer ver os dados de qual jogador? (999 para parar) '))
    if pesquisa == 999:
        break
    if pesquisa >= len(jogadores) or pesquisa < 0:
        print(f'Oops, parece que não existe esse jogador. ')
    else:
        print(f'Levantamento do jogador {jogadores[pesquisa]["nome"]}: ')
        for i, g in enumerate(jogadores[pesquisa]["gols"]):
            print(f'    No jogo {i+1} fez {g} gols')
        print('-=-' * 30)

print('Fim do Programa')
