# Autor: Giancarlo Massaccesi
# Data: 2025/06/03 
# Descrição: Projeto de treinamento DIO -  Métodos de Classe e Métodos Estáticos em Python

class Pessoa:

    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod # Método de classe
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano  # Considerando o ano atual como 2025
        return cls(nome, idade)
    
    @staticmethod # Método estático
    def e_maior_de_idade(idade):
        return idade >= 18

p = Pessoa.criar_de_data_nascimento(1981, 6, 6, 'Giancarlo')
print(p.nome, p.idade)  # Saída: Giancarlo 44

print(Pessoa.e_maior_de_idade(18))  # Saída: True
print(Pessoa.e_maior_de_idade(17))  # Saída: False
    