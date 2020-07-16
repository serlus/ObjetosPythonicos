alunos = [('Renzo', 0), ('luciano', 10), ('Ada', 9)]

print([(nome, nota)for nome, nota in alunos if nota > 5])  # list comprheetion
print([(fulano, valor)for fulano, valor in alunos if valor > 5])
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
