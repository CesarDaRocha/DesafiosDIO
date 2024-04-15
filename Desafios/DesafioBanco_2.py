
def depositar(dados_usuario, posicao_conta):

    while True:

        valor_deposito = float(input("\nDigite o valor a ser depositado: "))

        if valor_deposito > 0:

            dados_usuario[posicao_conta]['saldo_em_conta'] += valor_deposito
            dados_usuario[posicao_conta]['extrato'].append(f"+ R$ {str(valor_deposito)}")
            print(f"\nDepósito de R$ {valor_deposito:.2f} efetuado com sucesso!")

            return dados_usuario
        
        else:

            print("\nValor inválido!")


def sacar(dados_usuario, posicao_conta):

    while True:

        valor_saque = float(input("\nDigite o valor a ser sacado: "))

        if valor_saque > 0:

            dados_usuario[posicao_conta]['saldo_em_conta'] -= valor_saque

            dados_usuario[posicao_conta]['extrato'].append(f"- R$ {str(valor_saque)}")

            print(dados_usuario)

            return dados_usuario

        else:

            print("\nValor inválido!")


def extrato(dados_usuario, posicao_conta):

    for i in dados_usuario[posicao_conta]['extrato']:
        print(i)

    print(f"\nSeu saldo atual é: {dados_usuario[posicao_conta]['saldo_em_conta']:.2f}")


def menu_operacao(dados_usuario, posicao_conta):

    menu = """
================
[1] Depositar
[2] Sacar
[3] Extrato
[4] Voltar
[5] Sair
================

->"""
    while True:

        opcao_menu = int(input(menu))

        if opcao_menu == 1:

            dados_usuario = depositar(dados_usuario, posicao_conta)

        elif opcao_menu == 2:

            dados_usuario = sacar(dados_usuario, posicao_conta)

        elif opcao_menu == 3:

            extrato(dados_usuario, posicao_conta)

        elif opcao_menu == 4:

            return dados_usuario

        elif opcao_menu == 5:

            exit()


def cadastrar(dados_usuario):

    estados1 = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'ES', 'GO', 'MA']
    estados2 = ['MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS']
    estados3 = ['SC', 'SP', 'SE', 'TO', 'DF', 'RR', 'MS', 'MT', 'RO']
    estados_total = estados1 + estados2 + estados3

    while True:

        aux = 0
        cpf = int(input("\nDigite seu CPF: "))
        nome = str(input("\nDigite seu nome: "))
        senha = str(input("\nDigite sua senha: "))
        email = str(input("\nDigite seu email: "))
        estado = str.upper(input("\nDigite a sigla do seu estado: "))
        cidade = str(input("\nDigite sua cidade: "))

        if len(str(cpf)) == 11 and estado in estados_total:

            if len(dados_usuario) != 0:

                for i in range(len(dados_usuario)):

                    if dados_usuario[i]['cpf'] == cpf:
                        aux = 1
                        print("\nCPF já cadastrado!")
                        opcao_menu = int(input("\n[1] Tentar novamente\n[2] Sair\n-> "))

                        if opcao_menu == 2:

                            return dados_usuario
                        
                        elif opcao_menu == 1:

                            break                        
                    
                if aux != 1:

                    dados_usuario.append({'cpf': cpf, 'nome': nome, 'senha': senha, 'email': email, 'endereco': {'estado': estado, 'cidade': cidade}, 'saldo_em_conta': 0, 'extrato': []})
                    return dados_usuario
                    
            else:

                dados_usuario.append({'cpf': cpf, 'nome': nome, 'senha': senha, 'email': email, 'endereco': {'estado': estado, 'cidade': cidade}, 'saldo_em_conta': 0, 'extrato': []})
                print(dados_usuario)

                return dados_usuario

        else:

            print("\nErro! Verifique se o CPF ou o endereço está correto")
            if (int(input("\n[1] Tentar novamente\n[2] Voltar\n-> "))) == 2:

                break

def login(dados_usuario):

    aux = 0

    while True:
        
        cpf = int(input("\nDigite seu CPF: "))

        for i in range(len(dados_usuario)):
                
                if cpf == dados_usuario[i]['cpf']:

                    senha = str(input("\nDigite sua senha: "))

                    if dados_usuario[i]['senha'] == senha:
                        aux = 1
                        posicao_conta = i
                        break

        if aux == 1:

            dados_usuario = menu_operacao(dados_usuario, posicao_conta)
            return dados_usuario

        else:

            print("\nCPF ou senha invalido!!\n")


def menu(dados_usuario):

    menu_principal = """
==============
[1] Cadastrar
[2] Login
[3] Sair
==============

->"""

    while True:

        opcao_menu = int(input(menu_principal))

        if opcao_menu == 1:

            dados_usuario = cadastrar(dados_usuario)

        elif opcao_menu == 2:

            dados_usuario = login(dados_usuario)

        elif opcao_menu == 3:

            break


def inicializacao():

    dados_usuario = []


    menu(dados_usuario)


inicializacao()