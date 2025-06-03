# Autor: Giancarlo Massaccesi
# Data: 2025/06/02
# Descrição: Projeto de treinamento DIO sobre encapsulamento em Python

# Utilando de encapsulamento usando propriedades (properties) para controlar o acesso aos atributos


class Pessoa:
    def __init__(self, nome , ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
    @property
    def nome(self):
        return self._nome
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa('Giancarlo Massaccesi', 1980)
print(f'Nome: {pessoa.nome} \tIdade: {pessoa.idade} anos')
# Acesso ao atributo protegido através da propriedade