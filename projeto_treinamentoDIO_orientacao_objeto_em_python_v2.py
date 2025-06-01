# autor: Giancarlo Massaccesi
# data: 2025/05/31
# Descrição: Projeto de treinamento em Python com foco em orientação a objetos

# Desafio bicicletaria 

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor =  cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print('Buzinando!')
    
    def parar(self):
        print('Parando a bicicleta!')
        print('Bicicleta parada!')
    
    def correr(self):
        print('Acelerando a bicicleta!')
    
    def __str__(self):
        return f'Bicicleta {self.modelo} de cor {self.cor}, ano {self.ano}, valor R${self.valor:.2f}.'

#   def __str__(self):
#       return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
# outra forma de implementar o __str__
#       return f'Bicicleta(cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor})'


b1 = Bicicleta('vermelha', 'caloi', 2022, 600)
b1.buzinar()
b1.parar()
b1.correr()
print(f'Bicicleta {b1.modelo} de cor {b1.cor}, ano {b1.ano}, valor R${b1.valor:.2f}.')

b2 =Bicicleta('verde', 'monark', 2000, 189)
Bicicleta.buzinar(b2) # b2.buzinar() # Outra forma de chamar o método
print(b2)
