a = 5  # parametro declarado na global

def f(a=3):
    """variaveis globais em python são globais dentro do modulo apenas

    Args:
        a (int, optional): [mesmo atribuindo novo valor a uma variavel global dentro de uma função 
        ela não se altera. Apenas qd invocado o locals]. Defaults to 3.
    """
    print(globals())
    print(locals())
    print(a)

f()