nome = input('Digite seu nome completo: ').strip()
print('Ola {}.'.format(nome))
mai = nome.upper()
print('Seu nome em maiúsculo é: {}'.format(mai))
min = nome.lower()
print('Seu nome em minúsculo é: {}'.format(min))
qtdl = nome.split()
print('A quantidade de letras sem espaços é: {}'.format(len(nome) - nome.count(' ')))
lpri = len(qtdl[0])
print('O primeiro nome tem {} letras.'.format(lpri))
