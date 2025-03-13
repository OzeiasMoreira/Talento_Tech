class Livro:
    def __init__(self, titulo, autor, codigo):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = codigo

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_codigo(self):
        return self.__codigo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def exibir_informacoes(self):
        print(f"Título: {self.__titulo}")
        print(f"Autor: {self.__autor}")
        print(f"Código: {self.__codigo}")
