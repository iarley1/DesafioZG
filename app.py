def secao_1():
    return (
        "Erguei as mãos e dai glória a Deus\n"
        "Erguei as mãos e dai glória a Deus\n"
        "Erguei as mãos\n"
        "E cantai como os filhos do Senhor\n"
    )

def secao_2(nome1, nome2):
    return (
        "Os animaizinhos subiram de dois em dois\n"
        "Os animaizinhos subiram de dois em dois\n"
        f"{nome1}\n"
        f"E os {nome2}, como os filhos do Senhor\n"
    )
    

def secao_3():
    return (
        "Deus disse a Noé: Constrói uma arca\n"
        "Deus disse a Noé: Constrói uma arca\n"
        "Que seja feita\n"
        "De madeira para os filhos do Senhor\n"
    )
    

def secao_4(todos_muitos):
    return (
        "O senhor tem muitos filhos\n"
        f"{todos_muitos} filhos ele tem\n"
        "Eu sou um deles, você também\n"
        "Louvemos ao senhor\n"
    )
    
def bracos():
    return (
        "Braço direito, braço esquerdo"
    )

def pernas(numero):
    if numero == 1:
        return("Perna direita")
    else:
        return("Perna direita, perna esquerda")

def cabeca_voltinha(numero):
    if numero == 1:
        return("Balança a cabeça")
    else:
        return("Balança a cabeça, dá uma voltinha")

def pulinho_abraca(numero):
    if numero == 1:
        return("Dá um pulinho")
    else:
        return("Dá um pulinho e abraça o irmão")

def parte_1():
    return (
        "\n" +
        secao_1() + "\n" +
        secao_2("O elefante", "passarinhos") + "\n" +
        secao_2("A minhoquinha", "pinguins") + "\n" +
        secao_2("O canguru", "sapinho") + "\n" +
        secao_3() + "\n" +
        secao_1() + "\n" +
        secao_1() + "\n" +
        secao_1()
    )

def parte_2():
    return (
        "\n" +
        secao_4("Todos") + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(1) + "\n" + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(0) + "\n" + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(0) + "\n" + "\n" +
        cabeca_voltinha(1) + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(0) + "\n" + "\n" +
        cabeca_voltinha(0) + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(0) + "\n" +
        cabeca_voltinha(0) + "\n" +
        pulinho_abraca(1) + "\n" + "\n" +
        secao_4("Muitos") + "\n" +
        bracos() + "\n" + pernas(0) + "\n" +
        cabeca_voltinha(0) + "\n" +
        pulinho_abraca(0)
    )

def menu():
    print("Selecione uma opção:")
    print("1 - Imprimir a música completa")
    print("2 - Imprimir uma parte específica")
    opcao = int(input("Opção: "))

    if opcao == 1:
        print(parte_1() + parte_2())
    elif opcao == 2:
        numero_parte = int(input("Digite o número da parte que deseja imprimir: "))
        if numero_parte == 1:
            print(parte_1())
        elif numero_parte == 2:
            print(parte_2())
        else:
            print("Opção inválida!") 
    else:
        print("Opção inválida!")

menu()