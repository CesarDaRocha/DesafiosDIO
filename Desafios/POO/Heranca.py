#cor, placa, numero_rodas,          ligar motor         Caminhão, Moto, Carro

class Veiculo:

    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa 
        self.numero_rodas = numero_rodas

    def Ligar_motor(self):

        print("\nLigando...")
        print("\nLigado!\n")


class Caminhão(Veiculo):
    pass

class Moto(Veiculo):
    pass

class Carro(Veiculo):
    pass

moto1 = Moto("Vermelha", "HQN - 2509", 2)

moto1.Ligar_motor()




