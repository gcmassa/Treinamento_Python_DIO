# autor: Giancarlo Massaccesi
# DIO treinamento Python
# Projeto 2 - Controle de Saldo - identação, estruturas condicionais, estruturas de repetição

# Estruturas condicionais
saldo = 2000.00
saque =  float(input('Informe o valor do saque: '))

if saldo >= saque:
    saldo -= saque
    print(f'Saldo atual: {saldo:.2f}')
else:
    print('Saldo insuficiente!')
    print(f'Saldo atual: {saldo:.2f}')



# Maioridade
MAIOR_IDADE = 18
PERMISSAO = 17

idade = int(input('Informe a sua idade: '))

if idade >= MAIOR_IDADE:
    print('Maior de idade')
else:
    print('Menor de idade, ainda não pode dirigir')

if idade >= MAIOR_IDADE:
    print('Maior de idade')
elif idade == PERMISSAO:
        print('Menor de idade, pode dirigir com autorização')
else:
        print('Menor de idade, ainda não pode dirigir')
# Estruturas de repetição

# While
# while True:
#     print('Loop infinito')
#     break
# for i in range(10):
#     print(i)


# a = int(input('Informe um número: '))
# print(a)

# a += 1
# 1
# print(a)

#letra = p
#letra = y
#letra = t
#letra = h
#letra = o
#letra = n


texto =  input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
     if letra.upper() in VOGAIS:
          print(letra,end="")
else:
 print() # adiciona uma quebra de linha
 print('Fim do loop')

 # for letra in texto:

 for numero in range(0,51,5):
      print(numero, end=" ")

opcao = -1

while opcao != 0:
     opcao = int(input('[1] Sacar\n[2] Extrato\n[0] Sair\nEscolha uma opção: '))

     if opcao == 1:
          print('Sacando')
     elif opcao == 2:
          print('Exibindo extrato')
     else:
          print('Obrigado por usar o sistema!')

parouimpar = -1

while True:
     parouimpar = int(input('Informe um número: '))
     if parouimpar == 0:
          break
     elif parouimpar % 2 == 0:
          print('Número par')
     else:
          print('Número ímpar')