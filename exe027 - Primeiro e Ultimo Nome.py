nome = str(input('Digite um nome completo: ').strip())
separado = nome.split()
print('O primeiro nome é {}'.format(separado[0]))
print('O últido nome é {}'.format(separado[len(separado)-1]))
