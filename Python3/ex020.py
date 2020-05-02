from random import shuffle
aluno1 = input('Digite o nome do primeiro aluno:\n')
aluno2 = input('Digite o nome do segundo aluno:\n')
aluno3 = input('Digite o nome do terceiro aluno:\n')
aluno4 = input('Digite o nome do quarto aluno:\n')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('{} apagará o quadro.'.format(alunos))