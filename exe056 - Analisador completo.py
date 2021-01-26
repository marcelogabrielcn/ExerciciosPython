print('Bom dia, vamos analisar algumas informações!')
med = 0
mv = 0 # Idade do homem mais velho
hmv = ''  # nome do Homem mais velho
mmv = 0  # quantidade de mulheres maior de 20 anos
for ficha in range(1, 5):
    nome = str(input('Digite o nome da {}ª pessoa: ' .format(ficha)))
    idade = int(input('Digite a idade de {}: '.format(nome)))
    med += idade
    sexo = str(input('Sexo de {} [m/f]: '.format(nome))).lower()
    if sexo == 'm' and idade > mv:
        mv = idade
        hmv = nome
    elif sexo == 'f' and idade > 20:
        mmv += 1
print('Analisando essas informações, temos uma média de idades de {:.0f} anos.'.format(med / 4))
print('O homem mais velho é o {} que possui {} anos.'.format(hmv, mv))
print('Neste grupo tem {} mulher(es) acima dos 20 anos.'.format(mmv))
