# autor: Giancarlo Massaccesi
# data: 31/05/2025
# Treinamento Python Developer DIO Suzano
# programa orientado a objetos com construtores e destrutores em Python

# __init__ é o construtor da classe, chamado quando um objeto é criado
# __del__ é o destrutor da classe, chamado quando um objeto é destruído

class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando o objeto Cachorro...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
    
    def __del__(self):
        print('Destroi o objeto Cachorro...')

    def latir(self):
        print('Au Au!')

def criar_cachorro():
    c = Cachorro('Zeus', 'preto e branco', False)
    print(c.nome)

criar_cachorro()
#c = Cachorro('chappie', 'amarelo')
#c.latir()