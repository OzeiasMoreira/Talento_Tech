planetas = [

]

def menu():
    print("\nBem-Vindo ao sistema de Planetas do Talento Tech")
    print("\nO que deseja fazer?")
    print("1 - Adicionar Planeta")
    print("2 - Exibir Planetas")
    print("3 - Buscar Planeta por nome")
    print("4 - Alterar informações de um Planeta")
    print("5 - Excluir Planeta")
    print("6 - Sair")

def adicionar():
    nome = input("Nome do Planeta: ")
    massa = float(input("Massa(em Kg): "))
    raio = float(input("Raio(em Km):" ))
    distancia = float(input("Distancia em relação ao Sol(em Km): "))
    planetas.append({"nome": nome, "massa": massa, "raio": raio, "distancia": distancia})
    print(f"Planeta {nome} adicionado com sucesso!")

def exibir():
    if not planetas:
        print("Poxa que pena,nenhum Planeta ainda foi cadastrado.")
        return
    
    for planeta in planetas:
        print(f"\nNome: {planeta['nome']}")
        print(f"Massa: {planeta['massa']}Kg")
        print(f"Raio: {planeta['raio']} Km")
        print(f"Distancia do Sol:  {planeta['distancia']} milhões de Km")

def buscar(nome):
    for planeta in planetas:
        if planeta["nome"] == nome:
            return planeta
        
    return None

def atualizar():
    nome = input("Qual Planeta deseja atualizar?")
    planeta = buscar(nome)
    if planeta:
        print("Deixe em branco para manter o valor atual.")
        novaMassa = input(f"Massa atual ({planeta['massa']} kg): ")
        novoRaio = input(f"Raio atual ({planeta['raio']} km): ")
        novaDistancia = input(f"Distancia atual do Sol({planeta['distancia']} milhões de km): ")

        if novaMassa:
            planeta["massa"] = float(novaMassa)
        if novoRaio:
            planeta["raio"] = float(novoRaio)
        if novaDistancia:
            planeta["distancia"] = float(novaDistancia)

        print(f"Planeta {nome} foi atualizado com sucesso!")

    else:
        print("Planeta não encontrado.")

def excluir():
    nome = input("Qual Planeta deseja excluir?")
    planeta = buscar(nome)
    if planeta:
        planetas.remove(planeta)
        print(f"Planeta {nome} foi excluido com sucesso!")
    else:
        print(f"Planeta {nome} não encontrado.")


def main():
    while True:
        menu()
        opcao = input("O que deseja fazer?")

        if opcao == '1':
            adicionar()
        
        elif opcao == '2':
            exibir()

        elif opcao == '3':
            nome = input("Qual Planeta deseja buscar?")
            planeta = buscar(nome)
            if planeta:
                print(f"\nNome: {planeta['nome']}")
                print(f"Massa: {planeta['massa']}")
                print(f"Raio: {planeta['raio']}")
                print(f"Distancia: {planeta['distancia']}")

            else:
                print(f"Planeta {nome} não encontrado.")

        elif opcao == '4':
            atualizar()

        elif opcao == '5':
            excluir()

        elif opcao == '6':
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()

