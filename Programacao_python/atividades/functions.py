import math

def intervalo(inicio,final):
    soma = 0
    for i in range(inicio,final + 1):
        soma += i

    return soma

def media(inicio,final):
    total = (final - inicio) + 1
    soma = intervalo(inicio,final)

    return soma / total

def raizSoma(inicio,final):
    soma = intervalo(inicio,final)
    
    return math.sqrt(soma)

def main():
    inicio = int(input("Insira o número inicial:")) 
    final = int(input("Insira o número final: "))

    soma = intervalo(inicio,final)
    print(f"A soma de todos os números do {inicio} até o {final} é: {soma}")

    m = media(inicio,final)
    print(f"A média dos números no intervalo é: {m}")

    raiz = raizSoma(inicio,final)
    print(f"A raiz quadrada da soma é: {raiz}")


if __name__ == "__main__":
    main()    
    