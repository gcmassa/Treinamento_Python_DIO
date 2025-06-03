# Autor: Giancarlo Massaccesi
# Data: 2025/06/02
# Descrição: Projeto de treinamento DIO sobre encapsulamento em Python

# Utilando de encapsulamento usando propriedades (properties) para controlar o acesso aos atributos

class Foo:
    def __init__(self, x=None):
        self._x = x
    @property # Define uma propriedade para acessar o atributo protegido
    def x(self):
        return self._x or 0 # Retorna 0 se _x for None
    @x.setter # Define um setter para modificar o atributo protegido
    def x(self, value):
        self._x += value
    @x.deleter # Define um deleter para excluir o atributo protegido
    def x(self):
        self._x = -1  # Deleta o atributo protegido, atribuindo -1 como valor

foo = Foo(10)
print(foo.x)  # Acesso ao atributo protegido através da propriedade
foo.x = 10 # Acesso ao setter da propriedade
print(foo.x)  # Acesso ao atributo protegido através da propriedade
del foo.x  # Acesso ao deleter da propriedade
print(foo.x)  # Acesso ao atributo protegido após deleção, deve retornar -1