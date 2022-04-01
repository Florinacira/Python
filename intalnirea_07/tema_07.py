
from abc import ABC , abstractmethod
class FormaGeometrica(ABC):
    PI = 3.14

    def descriere(self):
        print('Cel mai probabil am colturi')

    @abstractmethod
    def aria(self):
      pass

class Patrat(FormaGeometrica):

    def descriere(self):
        print('Cel mai probabil am colturi')

    def aria(self):
        print(f'Aria este: {self.__latura * self.__latura}')

    def __init__(self,latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura este: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self,noua_latura):
        self.__latura = noua_latura
        print(f'Noua latura este: {self.__latura}')

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = None


class Cerc(FormaGeometrica):

    def descriere(self):
        print('Eu nu am colturi')

    def aria(self):
        print(f'Aria cercului = {self.PI * self.__raza}')

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza este:{self.__raza}')

    @raza.setter
    def raza(self,raza):
        self.__raza = raza
        print(f'Noua raza este: {self.__raza}')

    @raza.deleter
    def raza(self):
        print(f'Am sters raza')
        self.__raza = None


patrat = Patrat(10)
print(patrat.latura)
patrat.aria()
patrat.latura=8
del patrat.latura
patrat.latura
patrat.descriere()

cerc = Cerc(34)
cerc.raza
cerc.raza
cerc.raza = 12
del cerc.raza
cerc.raza
cerc.descriere()




