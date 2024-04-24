# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:


# TODO: Crie um loop para solicitar os itens ao usuário:

# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens


def main():
  
    itens = []
  
    for i in range(3):

        item = str(input())
        itens.append(item)
  
    print("Lista de Equipamentos:")  
    for item in itens:
    # Loop que percorre cada item na lista "itens"
        print(f"- {item }")


main()