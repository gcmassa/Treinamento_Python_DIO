# Autor: Giancarlo Massaccesi
# Data: 2025/06/03 
# Descrição: Projeto de treinamento DIO - Variáveis, Classe e Instância em Python

class Estudante:
    escola = 'DIO'  # Atributo de classe

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'Estudante: {self.nome}, Matrícula: {self.matricula}, Escola: {self.escola}'

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Criando instâncias da classe Estudante

aluno_1 = Estudante('Giancarlo', 1)
aluno_2 = Estudante('Gionavana', 2)
# Exibindo informações dos alunos
mostrar_valores(aluno_1, aluno_2) # Exibindo o atributo de classe

aluno_1.matricula = 3  # Alterando o atributo de instância
mostrar_valores(aluno_1, aluno_2)  # Exibindo novamente para ver a alteração
        