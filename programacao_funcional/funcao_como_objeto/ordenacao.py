alunos = [('Renzo', 0), ('luciano', 10), ('Ada', 9)]

alunos.sort(key=lambda aluno: aluno[1])  # metodo de alta ordem

print(alunos)

def por_nome(aluno):
    return aluno[0]

print(sorted(alunos, key=por_nome))  # função de alta ordem
