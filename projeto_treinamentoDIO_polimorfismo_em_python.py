# Autor: Giancarlo Massaccesi
# Data: 2025/06/03
# Descrição: Projeto de treinamento DIO - Polimorfismo em Python

class Passaro:
    def voar(self):
        print('Voa!')

class Pardal(Passaro):
    def voar(self):
        super().voar()  # Chama o método da classe base Passaro
        # Implementação específica do Pardal
        

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não voa!')

def plano_de_voo(obj):
    obj.voar()
# Testando o polimorfismo

p1 = Pardal()
p2 = Avestruz()

plano_de_voo(p1)
plano_de_voo(p2)