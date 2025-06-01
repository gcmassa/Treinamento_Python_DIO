# autor: Giancarlo Massaccesi
# data: 2025/06/01
# Descrição: Projeto de treinamento em Python com foco em herança e polimorfismo


class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print('Ligando o motor do veículo...')
    def __str__(self):
        return self.cor

class motocicleta(veiculo):
    pass 

class carro(veiculo):
    pass

class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} está carregado.')

#moto = motocicleta('preta', 'ABC-1234', 2)
#print(f'Motocicleta de cor {moto.cor}, placa {moto.placa}, número de rodas {moto.numero_rodas}.')
#moto.ligar_motor()

#carro1 = carro('branco', 'XYZ-5678', 4)	
#carro1.ligar_motor()

caminhao1 = caminhao('roxo', 'LMN-9012', 6, True)
caminhao1.ligar_motor() 
caminhao1.esta_carregado()
print(caminhao1)