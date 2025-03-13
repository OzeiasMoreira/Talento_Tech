class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0

    def mover(self, velocidade):
        self.velocidade = velocidade
        print(f"O veículo {self.modelo} está se movendo a {self.velocidade} km/h.")

    def parar(self):
        self.velocidade = 0
        print(f"O veículo {self.modelo} parou.")

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def ligar(self):
        print(f"O motor {self.tipo} de {self.potencia} cavalos está ligado.")

    def desligar(self):
        print(f"O motor {self.tipo} de {self.potencia} cavalos está desligado.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_de_portas, motor):
        super().__init__(marca, modelo, ano)
        self.numero_de_portas = numero_de_portas
        self.motor = motor

    def abrir_porta(self, numero_porta):
        if 1 <= numero_porta <= self.numero_de_portas:
            print(f"A porta {numero_porta} do carro {self.modelo} foi aberta.")
        else:
            print(f"Porta inválida. Este carro tem apenas {self.numero_de_portas} portas.")


if __name__ == "__main__":
    motor = Motor(tipo="V8", potencia=300)
    carro = Carro(marca="Ford", modelo="Mustang", ano=2023, numero_de_portas=2, motor=motor)

    motor.ligar()
    carro.mover(80)
