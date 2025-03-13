def menu():
    
    print("\nBem-Vindo a calculadora TalentoTech")
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Encerrar")

while True:    

    menu()

    operacao = input("\nQual o número da operação desejada?")

    if operacao == '5':
        print("Encerrando...")
        break

    num1 = float(input("Insira o primeiro número: "))
    num2 = float(input("Insira o segundo número: "))

    if operacao == '1':
        resultado = num1 + num2
        print(f"A soma de {num1} e {num2} é: {resultado}")

    elif operacao == '2':
        resultado = num1 - num2 
        print(f"A subtração de {num1} e {num2} é: {resultado}")   

    elif operacao == '3':
        resultado = num1 * num2
        print(f"A multiplicação de {num1} e {num2} é: {resultado}")

    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"A divisão de {num1} e {num2} é: {resultado}")

        else:
            print("Divisão por zero não é permitida!")  

    else:
        print("Opcão inválida!")      