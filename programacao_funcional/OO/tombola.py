
# TDD da tombola

"""Uma tombola pode ser criada da seguinte maneira:
>>> from random import shuffle
>>> t = Tombola()

Após a criação os itens da tombola são representados por uma lista vazia:
>>> t.itens
[]

Uma lista recém criada não possui elemntos. Portanto o método "carregada" retorna falso:
>>> t.carregada()
False

É possivel carregar itens através do método "carregar":
>>> itens = [1, 2]
>>> t.carregar(itens)
>>> t.itens
[1, 2]


Após a lista carregada o método "carregada" retorna verdadeiro:
>>> t.carregada()
True


Uma tombola mistura seus itens:
>>> def embaralhador_mock(lista):
...     lista[0], lista[-1] = lista[-1], lista[0]
>>> shuffle = embaralhador_mock
>>> t.itens
[1, 2]
>>> t.misturar()
>>> t.itens
[2, 1]

Uma tombola serve para sortear elementos:
>>> t.sortear()
1
>>> t.carregada()
True
>>> t.sortear()
2
>>> t.carregada()
False

"""
from random import shuffle

class Tombola:
    def __init__(self):
        self.itens = []
    
    def carregar(self, lista):
        self.itens = lista

    def carregada(self):
        return bool(self.itens)

    def misturar(self):
        shuffle(self.itens)

    def sortear(self):
        return self.itens.pop()

if __name__ == '__main__':
    Tombola()
    