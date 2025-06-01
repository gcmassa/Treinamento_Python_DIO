# autor: Giancarlo Massaccesi
# data: 31/05/2025
# Descrição: Projeto de treinamento em Python com foco em orientação a objetos


# Definição da classe Cachorro
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome =  nome
        self. cor = cor
        self.acordado = acordado
    def latir(self):
        print('Au Au!')
    def dormir(self):
        self.acordado = False
        print('Zzzzz...')


# Definição de Objetos da classe Cachorro
cao1 = Cachorro('chappie', 'amarelo', False)
cao2 = Cachorro('aladim', 'branco e preto')

# Exibição dos atributos dos objetos
print('=' * 100)

cao1.latir()

print(f'O cachorro {cao1.nome} é da cor {cao1.cor} e está {"acordado" if cao1.acordado else "dormindo"}.')
print('=' * 100)
print(f'O cachorro {cao2.nome} é da cor {cao2.cor} e está {"acordado" if cao2.acordado else "dormindo"}.')
print(cao2.acordado)
print('=' * 100)
cao2.dormir()
print(f'O cachorro {cao2.nome} é da cor {cao2.cor} e está {"acordado" if cao2.acordado else "dormindo"}.')
