alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt * lar
tinta = area / 2
print('A área da sua sala é de {}m² e são necessários {:.1f} litros de tinta para pinta-la.'.format(area, tinta))
