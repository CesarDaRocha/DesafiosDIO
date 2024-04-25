

class Bicicleta:

    def __init__(self, cor, ano, modelo, valor):
        
        self.cor = cor
        self.ano = ano
        self.modelo = modelo
        self.valor = valor

    def parar(self):
        print("Freiando...\n")
        print("Bicicleta parada!\n")

    def correr(self):
        print("Vrummmmm...\n")

    def buzinar(self):
        print("Plim plim!\n")

    def __str__(self):
        return f"\n{__class__.__name__}:\n\n{'\n'.join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}\n"




bicicleta_1 = Bicicleta("Azul", 2022, "monarkão", 500)

"""bicicleta_1.correr()
bicicleta_1.buzinar()
bicicleta_1.parar()"""

#print(f"Modelo: {bicicleta_1.modelo}\nAno: {bicicleta_1.ano}\nCor: {bicicleta_1.cor}\nPreço: {bicicleta_1.valor}\n")

print(bicicleta_1.__str__())





    
        