def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


# Programa principal
name = str(input('Nome do Jogador: ')).strip().capitalize()
goals = str(input('Número de Gols: '))
if goals.isnumeric():
    goals = int(goals)
else:
    goals = 0
ficha(name, goals)
