# Autor: Giancarlo Massaccesi
# Data: 2025/06/03 
# Descrição: Projeto de treinamento DIO - Classes Abstratas em Python

from abc import ABC, abstractmethod, abstractproperty
# Classes abstratas são classes que não podem ser instanciadas diretamente.

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('TV ligada!')
    def desligar(self):
        print('Desligando a TV...')
        print('TV desligada!')
    @property
    def marca(self):
        return 'Marca da TV: Samsung'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o ar-condicionado...')
        print('Ar-condicionado ligado!')
    def desligar(self):
        print('Desligando o ar-condicionado...')
        print('Ar-condicionado desligado!')
    @property
    def marca(self):
        return 'Marca do Ar-condicionado: LG'

controle = ControleTV()
controle.ligar()  # Chama o método ligar da classe ControleTV
controle.desligar()  # Chama o método desligar da classe ControleTV
print(controle.marca)  # Acessa a propriedade marca da classe ControleTV

controle = ControleArCondicionado()
controle.ligar()  # Chama o método ligar da classe ControleArCondicionado
controle.desligar()  # Chama o método desligar da classe ControleArCondicionado
print(controle.marca)  # Acessa a propriedade marca da classe ControleArCondicionado
# controle = ControleRemoto()  # Isso causaria um erro, pois ControleRemoto é uma classe abstrata e não pode ser instanciada.