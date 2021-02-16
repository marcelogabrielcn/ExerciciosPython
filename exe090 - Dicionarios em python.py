alunos = dict()
alunos['nome'] = str(input('Digite o nome do aluno: '))
alunos['media'] = float(input('Digite a média do aluno: '))
if alunos['media'] >= 7:
    alunos['situação'] = 'Aprovado'
elif 5 < alunos['media'] < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'
print('-=-' * 10)
print(f'{alunos["nome"]} teve média {alunos["media"]}')
print(f'Com isso sua situação é: {alunos["situação"]}')
