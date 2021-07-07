def voto(ano):
    from datetime import date
    year = date.today().year
    idade = year - ano
    if 18 <= idade < 65:
        print(f'Com {idade} anos o voto é Obrigatório.')
    elif (16 <= idade < 18) or idade >= 65:
        print(f'Com {idade} anos o voto é OPCIONAL.')
    else:
        print(f'Com menos de 16 o voto é NEGADO.')


ano = int(input('Digite o ano de nascimento: '))
voto(ano)
