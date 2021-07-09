from time import sleep

cores = ('\033[m',           # 0 = Sem cor
         '\033[0;30;41m',    # 1 = Vermelho
         '\033[0;30;42m',    # 2 = Verde
         '\033[0;30;43m',    # 3 = Amarelo
         '\033[0;30;44m',    # 4 = Azul
         '\033[0;30;45m',    # 5 = Roxo
         '\033[7;30m',       # 6 = Branco
         '\033[0;30;47m'     # 7 = Cinza
        )


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    sleep(1)
    print(cores[3], end='')
    help(com)
    print(cores[3], end='')


def titulo(txt, cor=0):
    tam = len(txt) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)
    print(cores[0], end='')


# Programa Principal
comando = ''
while True:
    titulo('SITEMA DE AJUDA PyHELP', 4)
    comando = str(input('Função ou biblioteca >> '))
    sleep(1)
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 7)
