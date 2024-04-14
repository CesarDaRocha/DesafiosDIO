historico = []
limite_de_deposito = 0
contador_saque = 0
limite_de_saque = 0


def deposito(valor_a_depositar, valor_em_conta):

        valor_em_conta += valor_a_depositar

        historico.append(+valor_a_depositar)

        print(f"\nDepósito de R$ {valor_a_depositar:.2f} efetuado com sucesso!\n\nSeu Saldo agora é de: R$ {valor_em_conta:.2f}\n")

        return valor_em_conta



def sacar(valor_a_sacar, valor_em_conta, limite_de_saque):

    if valor_a_sacar < valor_em_conta:

        if(valor_a_sacar <= limite_de_saque):
        
            historico.append(-valor_a_sacar)

            valor_em_conta -= valor_a_sacar

            print(f"\nSaque de R$ {valor_a_sacar:.2f} efetuado com sucesso!\n\nSeu saldo atual é de: R$ {valor_em_conta:.2f}\n")

            return valor_em_conta

        else:

            print(f"\nLimite de saque é de R$ {limite_de_saque}\n")

            return valor_em_conta

    else:

        print(f"\nSaldo insuficiente!\nSeu saldo atual é de: R${valor_em_conta:.2f}\n")

        return valor_em_conta
    


def extrato(valor_em_conta):

    for i in range(len(historico)):
        
        if historico[i] > 0:

            print(f"\n + R$ {historico[i]:.2f}\n")

        elif historico[i] < 0:

            print(f"\n - R$ {historico[i]*-1:.2f}\n")

    print(f"\nSaldo em conta : {valor_em_conta:.2f}\n")



def menu(valor_a_depositar, valor_em_conta, valor_a_sacar, limite_de_deposito, limite_de_saque, contador_saque):


    while True:

        print_menu = """
=======================
| [1] Depositar       |
| [2] Sacar           |
| [3] Extrato         |
| [4] Sair            |
=======================

->  """

        opcao = int(input(print_menu))
        print("\n")

        if opcao == 1:

            if limite_de_deposito < 10:

                valor_em_conta = deposito(float(input("\nDigite o valor a ser depositado: ")), valor_em_conta)
            
                limite_de_deposito += 1

            else:

                print("\nNão foi possivel realizar a operação! \n\nLimite de depósitos diários: 3/3\n")
            

        elif opcao == 2:

            if contador_saque < 3:

                valor_em_conta = sacar(float(input("\nDigite o valor a ser sacado: ")), valor_em_conta, limite_de_saque)

                contador_saque += 1

            else:

                print("\nNão foi possivel realizar a operação! \n\nLimite de saques diários: 3/3\n")

        
        elif opcao == 3:

            extrato(valor_em_conta)
        
        elif opcao == 4:

            print("\nOperação Finalizada!\n")

            break
        
        else:
            print("\nDigite uma opção válida!\n")

        nova_operacao = int(input("\nDigite '1' caso queira realizar uma nova operação\n\n"))

        if nova_operacao == 1:

            print("\n")

        else:

            print("\nOperação finalizada com sucesso!\n")
            break



menu(valor_a_depositar=0, valor_em_conta=0, valor_a_sacar=0, limite_de_deposito=0, limite_de_saque=500, contador_saque=0)

