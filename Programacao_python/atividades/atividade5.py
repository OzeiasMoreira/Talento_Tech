from abc import ABC, abstractmethod
import random

class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass


class PagamentoCartao(Pagamento):
    def __init__(self, numero_cartao):
        self.numero_cartao = numero_cartao

    def validar_cartao(self):

        return len(self.numero_cartao) == 16 and self.numero_cartao.isdigit()

    def processar_pagamento(self, valor):
      
        if self.validar_cartao():
            print(f"Pagamento de R${valor:.2f} processado com sucesso pelo cartão {self.numero_cartao[-4:]}.")
        else:
            print("Número do cartão inválido. Não foi possível processar o pagamento.")



class PagamentoBoleto(Pagamento):
    def __init__(self):
        self.codigo_barras = None

    def gerar_boleto(self):
        
        self.codigo_barras = "".join(str(random.randint(0, 9)) for _ in range(47))
        print(f"Boleto gerado com código de barras: {self.codigo_barras}")

    def processar_pagamento(self, valor):
        
        if self.codigo_barras:
            print(f"Pagamento de R${valor:.2f} processado com sucesso pelo boleto {self.codigo_barras}.")
        else:
            print("Código de barras não gerado. Não foi possível processar o pagamento.")


if __name__ == "__main__":
    
    cartao = PagamentoCartao("1234567890123456")
    cartao.processar_pagamento(100.0)

    boleto = PagamentoBoleto()
    boleto.gerar_boleto()
    boleto.processar_pagamento(200.0)
