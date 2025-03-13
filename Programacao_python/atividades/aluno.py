class Aluno:
    def __init__(self, nome, sobrenome, ra):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__ra = ra

    def get_nome(self):
        return self.__nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_ra(self):
        return self.__ra

    def set_nome(self, nome):
        self.__nome = nome

    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def set_ra(self, ra):
        self.__ra = ra

    def exibir_informacoes(self):
        print(f"Nome: {self.__nome} {self.__sobrenome}")
        print(f"RA: {self.__ra}")
