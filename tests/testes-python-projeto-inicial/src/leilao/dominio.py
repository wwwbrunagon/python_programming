import sys

class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances

# class Avalaiador: 

#     def __init__(self):
#         self.maior_lance = sys.float_info.min
#         self.menor_lance = sys.float_info.max

#     def avalia(self, leilao: Leilao):

#         for lance.valor in lielao.lances:

