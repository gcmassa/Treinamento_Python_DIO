# autor: Giancarlo Massaccesi
# data: 2025-05-30
# DIO Treinamento Python Developer Suzano
# Descrição: Sistema bancário simples em Python versão 2

import textwrap

def menu():
    menu = '''\n
    ===================== SITEMA BANCARIO SIMPLES =====================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar constas
    [6]\tNovo usuário
    [7]\tSair
    => '''
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito em:\tR$ {valor:.2f}\n'
        print('\n=== Depósito realizado com sucesso! ===')
    else:
        print('\n@@@ Operação inválida! Por favor informe um valor válido. @@@')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print('\n@@@ Operação inválida! Você não tem saldo suficiente. @@@')
    elif excedeu_limite:
        print('\n@@@ Operação inválida! O valor do saque excede o limite. @@@')
    elif excedeu_saques:
        print('\n@@@ Operação inválida! Número máximo de saques excedido. @@@')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque em:\tR$ {valor:.2f}\n'
        numero_saques += 1
        print('\n=== Saque realizado com sucesso! ===')
    else:
        print('\n@@@ Operação inválida! Por favor informe um valor válido. @@@')

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF <somente números>: ') 
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\n@@@ Já existe usuário com esse CPF. @@@')
        return
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento <dd-mm-yyyy>: ')
    endereco = input('Informe o endereço <logradouro, número - bairro - cidade/UF>: ')
    usuarios.append({'nome': nome, 'cpf': cpf, 'data_nascimento': data_nascimento, 'endereco': endereco})
    print('\n=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuarios['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print(f'\n=== Conta criada com sucesso! ===\nAgência:\t{agencia}\nNúmero da conta:\t{numero_conta}')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    print('\n@@@ Usuário não encontrado, operação de criação de conta encerrado. @@@')

def listar_contas(contas):
    for conta in contas:
        linha = f'''\n
                Agência:\t{conta['agencia']}
                Número da conta:\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
            '''
        print('=' * 100)
        print(textwrap.dedent(linha))


# definindo constantes
LIMITE_SAQUES = 3
AGENCIA = '0001'

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
usuarios = []
contas = []    

while True:
    opcao = menu()
    if opcao == 1:
     valor = float(input('Informe o valor a ser depositado: R$ '))
     saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == 2:
        valor = float(input('Informe o valor a ser sacado: R$ '))
        saldo, extrato = sacar(
        saldo = saldo,
        valor = valor,
        extrato = extrato,
        limite = limite,
        numero_saques = numero_saques,
        limite_saques = LIMITE_SAQUES
        )
    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)
    elif opcao == 4:
        criar_usuario(usuarios)
    elif opcao == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == 6:
        listar_contas(contas)
    elif opcao == 7:
        print('\n=== Sistema bancário encerrado. ===')
        break
    else:
            print('\n@@@ Opção inválida! Por favor, selecione uma opção válida. @@@')