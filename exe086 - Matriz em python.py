matriz = [[], [], [], [], [], [], [], [], []]
cont = 0
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[cont].append(int(input(f'Digite um valor para posição {linha}, {coluna}: ')))
        cont += 1
print('-=-' * 20)
print(f' { matriz[0] } { matriz[1]} { matriz[2]} '
      f'\n { matriz[3] } { matriz[4]} { matriz[5] } '
      f'\n { matriz[6] } { matriz[7]} { matriz[8] } ')
