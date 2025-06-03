# Autor: Giancarlo Massaccesi
# Data: 2025/06/02
# Descrição: Projeto de treinamento DIO sobre encapsulamento em Python

#class Conta:
#    def __init__(self, saldo=0):
#        self._saldo = saldo  # Atributo protegido
#    def depositar(self, valor):
#        self._saldo += valor  # Método para depositar, acessa o atributo protegido
#        return self._saldo
#    def sacar(self, valor):
#        pass

#conta = Conta(100)
#conta.depositar(100)
#print(conta._saldo)  # Acesso ao atributo protegido, não recomendado
#print(conta.depositar(100))  # Acesso ao método público que manipula o saldo

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo  # Atributo protegido
        self.nro_agencia = nro_agencia  # Atributo público
    def depositar(self, valor):
        # ...
        self._saldo += valor  # Método para depositar, acessa o atributo protegido
    def sacar(self, valor):
        # ...
        self._saldo -= valor  # Método para sacar, acessa o atributo protegido
    def mostrar_saldo(self):
        return self._saldo
    
conta = Conta('0001', 100)
conta.depositar(100)
print(conta.nro_agencia)  # Acesso ao atributo público
print(conta.mostrar_saldo())  # Acesso ao método público que retorna o saldo
# print(conta._saldo)  # Acesso ao atributo protegido, não recomendado