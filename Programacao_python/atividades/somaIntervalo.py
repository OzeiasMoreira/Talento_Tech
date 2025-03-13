inicio = int(input("Insira o número inicial: "))
final = int(input("Insira o número final: "))

soma = 0

for i in range(inicio,final + 1):
    soma += i

print(f"A soma de todos os números de {inicio} até {final} é: {soma}")