#definindo funções

# Definindo funções
# idade = 43
# Dio treinamento Python

# # projeto 5 - definindo funções

# # Nome: Giancarlo Massaccesi

def exibir_mensagem():
    print('Olá, mundo!')
    print('Bem-vindo ao curso de Python!')
    print('Vamos aprender a programar!')

def exibir_mensagem_2(nome):
    print(f'Seja bem vindo(a), {nome}!')

def exibir_mensagem_3(nome='Anonimo'):
    print(f'Seja bem vindo(a), {nome}!')
    
#exibir_mensagem()
#exibir_mensagem_2(nome='Giancarlo')
#exibir_mensagem_3()
#exibir_mensagem_3(nome='Teste')

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print('Ola Mundo!')
    return None

# Testando as funções
print(calcular_total([10,20,34])) # 64
print(retorna_antecessor_e_sucessor(10)) # (9, 11)
print(func_3()) # None

def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro {marca}/{modelo}/{ano}/{placa} salvo com sucesso!')

#salvar_carro('Wolkswagen', 'Fusca', 1970, 'ABC-1234')
#salvar_carro(marca='Wolkswagen', modelo='Fusca', ano=1970, placa='ABC-1234')
salvar_carro(**{'marca': 'Wolkswagen', 'modelo': 'Fusca', 'ano': 1970, 'placa': 'ABC-1234'})

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(mensagem)

exibir_poema('23 de Maio de 2025',
    'A vida é bela',
    'A vida é curta',
    'A vida é uma viagem',
    autor='Giancarlo Massaccesi',
    ano=2025)

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f'O resultado da operação é = {resultado}')

exibir_resultado(10, 10, somar) # 20
exibir_resultado(10, 10, subtrair) # 0
exibir_resultado(10, 10, multiplicar) # 100


op = somar
print(op(1, 23)) # 24


salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

salario_com_bonus = salario_bonus(500) # 2500
print(salario_com_bonus) # 2500
