# TDD da tombola

 Uma tombola pode ser criada da seguinte maneira:

```python
>>> from programacao_funcional.OO.tombola import Tombola
>>> t = Tombola()

```

Após a criação os itens da tombola são representados por uma lista vazia:

```python
>>> t.itens
[]

```

Uma lista recém criada não possui elemntos. Portanto o método "carregada" retorna falso:
```python
>>> t.carregada()
False

```

É possivel carregar itens através do método "carregar":

```python
>>> itens = [1, 2]
>>> t.carregar(itens)
>>> t.itens
[1, 2]

```
Após a lista carregada o método "carregada" retorna verdadeiro:

```python
>>> t.carregada()
True

```

Uma tombola mistura seus itens:
```python
>>> def embaralhador_mock(lista):
...     lista[0], lista[-1] = lista[-1], lista[0]
>>> tombola.shuffle = embaralhador_mock
>>> t.itens
[1, 2]
>>> t.misturar()
>>> t.itens
[2, 1]

```

Uma tombola serve para sortear elementos:
```python
>>> t.sortear()
1
>>> t.carregada()
True
>>> t.sortear()

```
