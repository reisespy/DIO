# -*- coding: utf-8 -*-
'''
Original file is located at
    https://colab.research.google.com/drive/199WWsHmm_-kA6lneM7BKMAxTeUTN8HNP

# -*- coding: UTF-8 -*-

SISTEMA BANCÁRIO - Banco ARCoin v0.1.3
Código desenvolvido por Ariel Reises
Para o curso de Python Developer - DIO
Campo Limpo Paulista, domingo, 13 de agosto de 2023
'''

# Importando as bibliotecas de data e calendário
import datetime

# Definindo a apresentação de data por extenso, em português.
def data_por_extenso(data):
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    dia_semana = dias[data.weekday()]
    dia = data.day
    mes = meses[data.month - 1]
    ano = data.year

    data_extenso = f"{dia_semana}, {dia} de {mes} de {ano}"

    return data_extenso

# Função para limpar a tela
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para a tela inicial
def tela_inicial():
    print("Bem-vindo ao Banco ARCoin!\n")
    print("Menu Inicial")
    print("Digite a opção desejada:\n")
    print("[1] Para entrar com CPF")
    print("[2] Para criar um novo cadastro")
    print("\n[0] Para sair")

# Função para a tela de cadastro
def tela_de_cadastro():
    print("\nObrigado pelo interesse em ser cliente do Banco ARCoin!\n")
    print("No momento, não estamos realizando cadastros de novos clientes.")
    print("Entre em contato com nossa central de atendimento para realizar seu cadastro")
    print("(11) 9 6379-1919\n")

# Variáveis de login - Posteriormente, farei um banco de dados.
CPF_CLIENTE = "39601628800"
NOME = "Ariel"
SOBRENOME = "Ladislau Reises"
SENHA = "637919"

# Função para a tela de login
def tela_de_login():
    print("\nOlá, cliente ARCoin\n")
    cpf_login = input("Insira o número do seu CPF para continuar (ou '0' para voltar ao menu inicial): ")

    if cpf_login == '0':
        return  # Volta ao menu inicial

    if len(cpf_login) == 11 and cpf_login == CPF_CLIENTE:
        tentativas = 0
        while tentativas < 3:
            senha_correta = input("Insira sua senha: ")

            if len(senha_correta) == 6 and senha_correta == SENHA:
                print(f"\nBem-vindo de volta, {NOME} {SOBRENOME}!")
                gerenciar_conta_bancaria()
                break  # Sai do loop após login bem-sucedido
            elif len(senha_correta) < 6 or len(senha_correta) > 6:
                print("\nA senha deve conter 6 dígitos.\n")
            else:
                print("Senha incorreta. Tente novamente.\n")
                tentativas += 1

        if tentativas == 3:
            print("\nVocê excedeu o número máximo de tentativas e seu login foi bloqueado.")
            print("Entre em contato com nossa central de relacionamento pelo telefone: (11) 9 6379-1919")
            return

    elif len(cpf_login) < 11 or len(cpf_login) > 11:
        print("\nO formato do CPF digitado é inválido, revise o número digitado.\n")
    else:
        print("\nCPF não cadastrado.\n")

# Main loop
while True:
    limpar_tela()
    tela_inicial()

    escolha = input("\nOpção desejada: ")

    if escolha == '1':
        limpar_tela()
        tela_de_login()
        input("Pressione Enter para continuar...")
    elif escolha == '2':
        limpar_tela()
        tela_de_cadastro()
        input("Pressione Enter para continuar...")
    elif escolha == '0':
        print("\nObrigado por utilizar o Banco ARCoin")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Função para imprimir o extrato
def imprimir_extrato(extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print("=========================================")

# Função para gerenciar a conta bancária
def gerenciar_conta_bancaria():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques_dia = 0
    LIMITE_SAQUES_DIA = 3
    ultimo_dia_saque = None

    while True:
        limpar_tela()

        data_atual = datetime.datetime.now()
        data_extenso = data_por_extenso(data_atual)

        menu = f"""
================= MENU =================

Olá, {NOME}!
Hoje é {data_extenso}

Escolha uma das opções abaixo:

[1] Depositar valor em conta
[2] Sacar dinheiro
[3] Exibir o extrato bancário

[0] Sair
========================================
===> """

        opcao = input(menu)

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f} - Saldo anterior: R$ {saldo - valor:.2f}")
                imprimir_extrato(extrato)
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == '2':
            if numero_saques_dia >= LIMITE_SAQUES_DIA:
                print(f"{NOME}, o seu limite diário de 3 saques foi excedido. Volte amanhã.")
            else:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo_disponivel = saldo + limite

                if valor > saldo_disponivel:
                    print("Operação falhou! Você não possui saldo e limite suficientes em conta.")
                elif valor > 0:
                    if valor <= saldo:
                        saldo -= valor
                        extrato.append(f"Saque efetuado: R$ {valor:.2f} - Saldo anterior: R$ {saldo + valor:.2f}")
                    else:
                        limite -= (valor - saldo)
                        saldo = 0
                        extrato.append(f"Saque efetuado (utilizando limite): R$ {valor:.2f} - Saldo anterior: R$ {saldo:.2f}")

                    numero_saques_dia += 1
                    imprimir_extrato(extrato)

                else:
                    print("Operação falhou! O valor informado é inválido.")

        elif opcao == '3':
            imprimir_extrato(extrato)
            print(f"\nSaldo disponível: R$ {saldo:.2f}")
            print(f"\nLimite disponível: R$ {limite:.2f}")
            print(f"\nSaldo disponível (com o limite): R$ {saldo + limite:.2f}")

        elif opcao == '0':
            print("Obrigado por utilizar o Banco ARCoin")
            break

        else:
            print("Operação inválida! Selecione novamente a operação desejada.")


# Assinatura - Ariel Reises
print("")
print("Obrigado por utilizar o sistema")
print("Copyright © 2023 - reises.py")

"""# Código detalhado"""

# -*- coding: UTF-8 -*-
"""
SISTEMA BANCÁRIO - Banco ARCoin v0.1.3
Código desenvolvido por Ariel Reises
Para o curso de Python Developer - DIO
13/08/2023
"""

# Importando as bibliotecas de data e calendário
import datetime

# Definindo a apresentação de data por extenso, em português.
def data_por_extenso(data):
    dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    dia_semana = dias[data.weekday()]
    dia = data.day
    mes = meses[data.month - 1]
    ano = data.year

    data_extenso = f"{dia_semana}, {dia} de {mes} de {ano}"

    return data_extenso

# Função para limpar a tela
def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para a tela inicial
def tela_inicial():
    print("Bem-vindo ao Banco ARCoin!\n")
    print("Menu Inicial")
    print("Digite a opção desejada:\n")
    print("[1] Para entrar com CPF")
    print("[2] Para criar um novo cadastro")
    print("\n[0] Para sair")

# Função para a tela de cadastro
def tela_de_cadastro():
    print("\nObrigado pelo interesse em ser cliente do Banco ARCoin!\n")
    print("No momento, não estamos realizando cadastros de novos clientes.")
    print("Entre em contato com nossa central de atendimento para realizar seu cadastro")
    print("(11) 9 6379-1919\n")

# Função para imprimir o extrato
def imprimir_extrato(extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for movimento in extrato:
            print(movimento)
    print("=========================================")

# Variáveis de login - Posteriormente, farei um banco de dados.
CPF_CLIENTE = "39601628800"
NOME = "Ariel"
SOBRENOME = "Ladislau Reises"
SENHA = "637919"

# Função para a tela de login
def tela_de_login():
    print("\nOlá, cliente ARCoin\n")
    cpf_login = input("Insira o número do seu CPF para continuar (ou '0' para voltar ao menu inicial): ")

    if cpf_login == '0':
        return  # Volta ao menu inicial

    if len(cpf_login) == 11 and cpf_login == CPF_CLIENTE:
        tentativas = 0
        while tentativas < 3:
            senha_correta = input("Insira sua senha: ")

            if len(senha_correta) == 6 and senha_correta == SENHA:
                print(f"\nBem-vindo de volta, {NOME} {SOBRENOME}!")
                gerenciar_conta_bancaria()
                break  # Sai do loop após login bem-sucedido
            elif len(senha_correta) < 6 or len(senha_correta) > 6:
                print("\nA senha deve conter 6 dígitos.\n")
            else:
                print("Senha incorreta. Tente novamente.\n")
                tentativas += 1

        if tentativas == 3:
            print("\nVocê excedeu o número máximo de tentativas e seu login foi bloqueado.")
            print("Entre em contato com nossa central de relacionamento pelo telefone: (11) 9 6379-1919")
            return

    elif len(cpf_login) < 11 or len(cpf_login) > 11:
        print("\nO formato do CPF digitado é inválido, revise o número digitado.\n")
    else:
        print("\nCPF não cadastrado.\n")

# Main loop
while True:
    limpar_tela()
    tela_inicial()

    escolha = input("\nOpção desejada: ")

    if escolha == '1':
        limpar_tela()
        tela_de_login()
        input("Pressione Enter para continuar...")
    elif escolha == '2':
        limpar_tela()
        tela_de_cadastro()
        input("Pressione Enter para continuar...")
    elif escolha == '0':
        print("\nObrigado por utilizar o Banco ARCoin")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Função para gerenciar a conta bancária
def gerenciar_conta_bancaria():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques_dia = 0
    LIMITE_SAQUES_DIA = 3
    ultimo_dia_saque = None

    while True:
        limpar_tela()

        data_atual = datetime.datetime.now()
        data_extenso = data_por_extenso(data_atual)

        menu = f"""
================= MENU =================

Olá, {NOME}!
Hoje é {data_extenso}

Escolha uma das opções abaixo:

[1] Depositar valor em conta
[2] Sacar dinheiro
[3] Exibir o extrato bancário

[0] Sair
========================================
===> """

        opcao = input(menu)

        if opcao == '1':
            valor = float(input("Informe o valor do depósito: R$ "))

            if valor > 0:
                saldo += valor
                extrato.append(f"Depósito: R$ {valor:.2f} - Saldo anterior: R$ {saldo - valor:.2f}")
                imprimir_extrato(extrato)
            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == '2':
            if numero_saques_dia >= LIMITE_SAQUES_DIA:
                print(f"{NOME}, o seu limite diário de 3 saques foi excedido. Volte amanhã.")
            else:
                valor = float(input("Informe o valor do saque: R$ "))
                saldo_disponivel = saldo + limite

                if valor > saldo_disponivel:
                    print("Operação falhou! Você não possui saldo e limite suficientes em conta.")
                elif valor > 0:
                    if valor <= saldo:
                        saldo -= valor
                        extrato.append(f"Saque efetuado: R$ {valor:.2f} - Saldo anterior: R$ {saldo + valor:.2f}")
                    else:
                        limite -= (valor - saldo)
                        saldo = 0
                        extrato.append(f"Saque efetuado (utilizando limite): R$ {valor:.2f} - Saldo anterior: R$ {saldo:.2f}")

                    numero_saques_dia += 1
                    imprimir_extrato(extrato)

                else:
                    print("Operação falhou! O valor informado é inválido.")

        elif opcao == '3':
            imprimir_extrato(extrato)
            print(f"\nSaldo disponível: R$ {saldo:.2f}")
            print(f"\nLimite disponível: R$ {limite:.2f}")
            print(f"\nSaldo disponível (com o limite): R$ {saldo + limite:.2f}")

        elif opcao == '0':
            print("Obrigado por utilizar o Banco ARCoin")
            break

        else:
            print("Operação inválida! Selecione novamente a operação desejada.")

# Assinatura - Ariel Reises
print("")
print("Obrigado por utilizar o sistema")
print("Copyright © 2023 - reises.py")