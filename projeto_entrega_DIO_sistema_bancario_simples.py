# autor: Giancarlo Massaccesi
# data: 2025-05-24
# DIO Treinamento Python Developer Suzano
# Descrição: Sistema bancário simples em Python

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

Escolha uma opção: """

# variaveis

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:

        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor informado inválido! Tente novamente.")
    elif opcao == 2:

        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_de_saques >= LIMITE_DE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. ")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido. ")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        else:
            print("Valor informado inválido! Tente novamente. ")
    elif opcao == 3:
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == 4:
        print("Obrigado por usar o sistema! Até logo.")
        break
    else:
        print("Opção inválida! Tente novamente.")
# Fim do código