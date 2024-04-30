#Conta Bancaria

class Usuarios_Geral:

    def __init__(self, nome_usuario, cpf_usuario, email_usuario, senha):
        
        self.nome_usuario = nome_usuario
        self.cpf_usuario = cpf_usuario
        self.email_usuario = email_usuario
        self.senha = senha

class Usuario_cliente(Usuarios_Geral):

    def __init__(self, nome_usuario, cpf_usuario, email_usuario, senha, numero_conta, agencia, saldo_conta):
        super().__init__(nome_usuario, cpf_usuario, email_usuario, senha)
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo_conta = saldo_conta



    def Sacar(self):

        valor_sacar = float(input("\nValor a sacar: "))

        if valor_sacar < self._saldo_conta and valor_sacar > 0:

            self._saldo_conta -= valor_sacar
            print("\nSaque efetuado!\n\n")
            print(f"Seu saldo atual é de:{self._saldo_conta}")
            return self._saldo_conta
        
        elif valor_sacar <= 0:

            print("\nErro! O valor a ser sacado deve ser maior que 0.")
            return
        
        elif valor_sacar > self._saldo_conta:

            print("Erro! Saldo insuficiente.")
            return
        else:

            print("\nErro desconhecido!")
        
    def Depositar(self):

        valor_depositar = float(input("\nValor a ser depositado: "))

        if valor_depositar > 0 and valor_depositar <= 10000:

            self._saldo_conta += valor_depositar
            print("\nDeposito efetuado!\n\n")
            print(f"Seu saldo atual é de: {self._saldo_conta}\n\n")
            return self._saldo_conta
        
        elif valor_depositar > 10000:
            
            print("\nErro! Não é possivel depositar valores acima de R$ 10.000")

        elif valor_depositar <= 0:

            print("\nNão foi possivel efetuar o deposito")

        else:

            print("Erro desconhecido!")


    def __str__(self):
        return f"\n{__class__.__name__}:\n\n{'\n'.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}\n"


pessoa_1 = Usuario_cliente("Cesar", 71389771156, "cesartapuio@gmail.com", "carretao", 202200030, "00001", 300)

print(pessoa_1.__str__())


    

    

    