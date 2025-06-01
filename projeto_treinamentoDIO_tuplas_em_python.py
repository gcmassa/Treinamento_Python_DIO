#treinamento Python DIO
# Tuplas em Python

frutas = ('laranja', 'pera', 'uva',)

frutas[0] # acessa o primeiro elemento da tupla
frutas[2] # acessa o terceiro elemento da tupla

letras = tuple('python')

numeros = tuple([1, 2, 3, 4])

pais = ('Brasil',)

matriz = (
(1, "a", 2),
("b", 3, 4),
(5, 6, "c"),
)

matriz[0] # acessa a primeira linha da matriz
matriz[0][0] # acessa o primeiro elemento da primeira linha da matriz
matriz[0][-1] # acessa o último elemento da primeira linha da matriz
matriz[-1][-1] # acessa o último elemento da última linha da matriz
# Tuplas são imutáveis, não é possível alterar seus elementos
# Tuplas são iteráveis, é possível percorrer seus elementos

tupla = ('p', 'y', 't', 'h', 'o', 'n')

tupla[2:] # acessa os elementos a partir do terceiro elemento
tupla[:2] # acessa os dois primeiros elementos
tupla[1:3] # acessa os elementos do segundo ao terceiro
tupla[0:3:2] # acessa os elementos do primeiro ao terceiro, pulando de dois em dois
tupla[::] # acessa todos os elementos
tupla[::-1] # acessa todos os elementos na ordem inversa
tupla[-1] # acessa o último elemento

carros = ('gol', 'celta', 'palio',)

for indice, carro in enumerate(carros):
    print(f'Carro {indice}: {carro}')