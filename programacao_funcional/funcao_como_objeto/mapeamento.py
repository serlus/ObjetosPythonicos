import operator


alunos = [('Renzo', 0), ('luciano', 10), ('Ada', 9)]

print([nome for nome, nota in alunos if nota > 5])  # list comprheetion
"""basicamento é para empregar a condição boleana 'nota > 5'
todo o restante é uma list compreetion para empregar essa condição
"""


def possui_nota_maior_que_5(aluno):
    """Função q seleciona alunos

    Args:
        aluno ([type]): [description]

    Returns:
        [type]: [description]
    """
    _, nota=aluno
    return nota > 5


print(list(filter(possui_nota_maior_que_5, alunos)))  # funcional
# recebe uma função no 1º parametro um iteravel no 2º

def extrair_nome(aluno):
    nome, _ = aluno
    return nome


print(list(map(extrair_nome, alunos)))  # funcional


def extrair_nome(aluno):
    nome, _ = aluno
    return nome


print(list(map(extrair_nome, filter(possui_nota_maior_que_5, alunos))))  # funcional

print(list(map(operator.itemgetter(0), filter(possui_nota_maior_que_5, alunos))))  # funcional
