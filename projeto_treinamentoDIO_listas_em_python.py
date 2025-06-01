# Lista, tuplas, conjuntos, funções e dicionários

frutas = [ "laranja", "maçã", "uva"]
print(frutas)
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-2])

frutas = []
print(frutas)

letras = list("python")
print(letras)

lista = ["p","y", "t", "h", "o", "n"]
lista[2:] # Pega do índice 2 até o final
lista[:2] # Pega do início até o índice 2
lista[1:3] # Pega do índice 1 ao 3
lista[0:3:2] # Pula de 2 em 2
lista[::]  # Pega a lista inteira
lista[::-1]  # Inverte a lista

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Campo Grande", True]
print(carro)

carros = ["gol", "celta", "uno", "palio", "fiorino"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}, {carro}")


# listar apenas os números pares de uma lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

#versao com list comprehension
pares = [numero for numero in numeros if numero % 2 == 0]

# lista elevada ao quadrado

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)

#versao com list comprehension
quadrado = [numero ** 2 for numero in numeros]

nova_lista = []

nova_lista.append(1)
nova_lista.append("Python")
nova_lista.append([40, 30, 20])

print(nova_lista)
# Adicionando elementos na lista

print(nova_lista)

nova_lista.clear()  # Limpa a lista
print(nova_lista)

nova_lista = [1, "Python", [40, 30, 20]]

l2 = nova_lista.copy()  # Cria uma cópia da lista

print(nova_lista)

print(id(l2), id(nova_lista))  # Verifica se são o mesmo objeto
print(l2 is nova_lista)  # Verifica se são o mesmo objeto

l2[0] = 2  # Modifica o primeiro elemento da lista l2
print(l2)
print(nova_lista)  # nova_lista não foi alterada
print(l2 == nova_lista)  # Verifica se os valores são iguais

cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # Conta quantas vezes o elemento aparece na lista
print(cores.count("azul"))  # Conta quantas vezes o elemento aparece na lista
print(cores.count("verde"))  # Conta quantas vezes o elemento aparece na lista

linguagens = ["Python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp"]) # Adiciona os elementos da lista ao final da lista

print(linguagens)

print(linguagens.index("java"))  # Retorna o índice do elemento na lista
print(linguagens.index("Python"))  # Retorna o índice do elemento na lista

print(linguagens.pop())  # Remove o último elemento da lista e retorna o valor
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))  # Remove o elemento do índice 0 e retorna o valor

linguagens = ["Python", "js", "c", "java", "csharp"]

linguagens.remove("c")  # Remove o elemento da lista
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]

linguagens.reverse()  # Inverte a lista
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort()  # Ordena a lista

print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # Ordena a lista em ordem decrescente
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # Ordena a lista pelo tamanho dos elementos
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena a lista pelo tamanho dos elementos em ordem decrescente
print(linguagens)

linguagens = ["Python", "js", "c", "java", "csharp"]

print(len(linguagens))  # Retorna o tamanho da lista

print(sorted(linguagens, key=lambda x: len(x)))  # Retorna uma nova lista ordenada pelo tamanho dos elementos
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # Retorna uma nova lista ordenada pelo tamanho dos elementos em ordem decrescente