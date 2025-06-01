# Treinamento Python DIO - Projeto Conjuntos em Python
# Conjuntos em Python   

set([1, 2, 3, 1, 3, 4]) # Cria um conjunto, removendo duplicatas

set("abacaxi") # Cria um conjunto a partir de uma string, removendo duplicatas

set(("palio", "gol", "celta", "palio",)) # Cria um conjunto a partir de uma tupla, removendo duplicatas	

numeros = set([1, 2, 3, 1, 3, 4]) # Cria um conjunto a partir de uma lista, removendo duplicatas
print(numeros) # Exibe o conjunto

letras = set("abacaxi") # Cria um conjunto a partir de uma string, removendo duplicatas
print(letras) # Exibe o conjunto

carros = set(("palio", "gol", "celta", "palio",)) # Cria um conjunto a partir de uma tupla, removendo duplicatas
print(carros) # Exibe o conjunto

linguagens = set(["python", "java", "c++", "python"]) # Cria um conjunto a partir de uma lista, removendo duplicatas
print(linguagens) # Exibe o conjunto

numeros2 = {1, 2, 3, 2} # Cria um conjunto usando chaves, removendo duplicatas

numeros2 = list(numeros2) # Converte o conjunto em uma lista

print(numeros2[0]) # Exibe o primeiro elemento da lista

carros2 = {"gol", "celta", "palio"} # Cria um conjunto usando chaves, removendo duplicatas	

for carro in carros2: # Percorre o conjunto de carros
    print(carro) # Exibe cada carro do conjunto

for indice, carro in enumerate(carros2): # Percorre o conjunto de carros com índice
    print(f'Carro {indice}: {carro}') # Exibe o índice e o carro correspondente

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # União dos conjuntos, combina todos os elementos

print(conjunto_a.union(conjunto_b)) # Exibe a união dos conjuntos

conjunto_a = {1, 2, 3 }
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b) # Interseção dos conjuntos, retorna elementos comuns
print(conjunto_a.intersection(conjunto_b)) # Exibe a interseção dos conjuntos

conjunto_a.difference(conjunto_b) # Diferença dos conjuntos, retorna elementos únicos do conjunto_a
print(conjunto_a.difference(conjunto_b)) # Exibe a diferença dos conjuntos

conjunto_b.difference(conjunto_a) # Diferença dos conjuntos, retorna elementos únicos do conjunto_b
print(conjunto_b.difference(conjunto_a)) # Exibe a diferença dos conjuntos

conjunto_a.symmetric_difference(conjunto_b) # Diferença simétrica, retorna elementos únicos de ambos os conjuntos
print(conjunto_a.symmetric_difference(conjunto_b)) # Exibe a diferença simétrica dos conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # Verifica se conjunto_a é subconjunto de conjunto_b
print(conjunto_a.issubset(conjunto_b)) # Exibe se conjunto_a é subconjunto de conjunto_b

conjunto_b.issubset(conjunto_a) # Verifica se conjunto_b é subconjunto de conjunto_a
print(conjunto_b.issubset(conjunto_a)) # Exibe se conjunto_b é subconjunto de conjunto_a

conjunto_a.issuperset(conjunto_b) # Verifica se conjunto_a é superconjunto de conjunto_b
print(conjunto_a.issuperset(conjunto_b)) # Exibe se conjunto_a é superconjunto de conjunto_b

conjunto_b.issuperset(conjunto_a) # Verifica se conjunto_b é superconjunto de conjunto_a
print(conjunto_b.issuperset(conjunto_a)) # Exibe se conjunto_b é superconjunto de conjunto_a

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b) # Verifica se os conjuntos não têm elementos em comum
print(conjunto_a.isdisjoint(conjunto_b)) # Exibe se conjunto_a e conjunto_b não têm elementos em comum

conjunto_a.isdisjoint(conjunto_c) # Verifica se os conjuntos não têm elementos em comum
print(conjunto_a.isdisjoint(conjunto_c)) # Exibe se conjunto_a e conjunto_c não têm elementos em comum

sorteio = {1, 23}

sorteio.add(25) # Adiciona um elemento ao conjunto
print(sorteio) # Exibe o conjunto após a adição

sorteio.add(42) # Adiciona outro elemento ao conjunto
print(sorteio) # Exibe o conjunto após a adição

sorteio.add(25) # Tenta adicionar um elemento já existente, não terá efeito
print(sorteio) # Exibe o conjunto, sem alteração

sorteio = {1, 23}

print(sorteio) # Exibe o conjunto original

sorteio.clear() # Limpa todos os elementos do conjunto
print(sorteio) # Exibe o conjunto após a limpeza, que estará vazio

sorteio = {1, 23}

sorteio.copy() # Cria uma cópia do conjunto
copia_sorteio = sorteio.copy() # Armazena a cópia em uma nova variável
print(copia_sorteio) # Exibe a cópia do conjunto

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} # Cria um conjunto com números, removendo duplicatas

print(numeros) # Exibe o conjunto de números

numeros.discard(1) # Remove o elemento 1 do conjunto, se existir
print(numeros) # Exibe o conjunto após a remoção do elemento 1

numeros.discard(45) # Tenta remover o elemento 45, que não existe no conjunto, não terá efeito
print(numeros) # Exibe o conjunto, sem alteração

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} # Cria um conjunto com números, removendo duplicatas

print(numeros) # Exibe o conjunto de números
print(numeros.pop()) # Remove e retorna um elemento aleatório do conjunto
print(numeros.pop()) # Remove e retorna outro elemento aleatório do conjunto
print(numeros) # Exibe o conjunto após a remoção de elementos aleatórios

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} # Cria um conjunto com números, removendo duplicatas
print(numeros) # Exibe o conjunto de números
print(numeros.remove(0)) # Remove o elemento 0 do conjunto, se existir
print(numeros) # Exibe o conjunto após a remoção do elemento 0

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0} # Cria um conjunto com números, removendo duplicatas

len(numeros) # Retorna o número de elementos no conjunto
print(len(numeros)) # Exibe o número de elementos no conjunto

1 in numeros # Verifica se o elemento 1 está presente no conjunto
print(1 in numeros) # Exibe se o elemento 1 está presente no conjunto
10 in numeros # Verifica se o elemento 10 está presente no conjunto
print(10 in numeros) # Exibe se o elemento 10 está presente no conjunto