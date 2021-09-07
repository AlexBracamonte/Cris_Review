import logging
import math

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(message)s - %(processName)s',
)


class Poligonos:
    def __init__(self, lados: int, longitud: int):
        self.Nlados = lados
        self.longitud = longitud

    @staticmethod
    def perimetro(n, valor):
        x = n*valor
        print(f'Soy un poligono con perimetro: {x} u')

    @staticmethod
    def area(x):
        print(f'Soy un poligono con área: {x} u²')


class Triangulo(Poligonos):
    def __init__(self, longitud):

        Poligonos.__init__(self, 3, longitud)
        self.altura = self.longitud*(.5*3**.5)

    def calcular_area(self):
        x = (self.altura*self.longitud)/2
        self.area(x)

    def calcular_perimetro(self):
        self.perimetro(self.Nlados, self.longitud)


class Cuadrado(Poligonos):
    def __init__(self, lados, longitud):
        Poligonos.__init__(self, lados, longitud)

    def calcular_area(self):
        x = self.longitud**2
        self.area(x)

    def calcular_perimetro(self):
        self.perimetro(self.Nlados, self.longitud)


class Pentagono(Poligonos):
    def __init__(self, lados, longitud):
        Poligonos.__init__(self, lados, longitud)

    def calcular_area(self):
        print((2*math.tan(math.radians(36))))
        ap = self.longitud/(2*math.tan(math.radians(36)))
        x = self.longitud*5*ap/2
        self.area(x)

    def calcular_perimetro(self):
        self.perimetro(self.Nlados, self.longitud)


if __name__ == '__main__':
    logging.debug("Ejemplo con triangulo")
    base = int(input('Ingresa la longitud de un lado: '))
    triangulo1 = Triangulo(base)
    triangulo1.calcular_area()
    triangulo1.calcular_perimetro()

    logging.debug("Ejemplo con cuadrado")
    base = int(input('Ingresa la longitud de un lado: '))
    cuadrado1 = Cuadrado(4, base)
    cuadrado1.calcular_perimetro()
    cuadrado1.calcular_area()

    logging.debug("Ejemplo con pentagono")
    base = int(input('Ingresa la longitud de un lado: '))
    pentagono1 = Pentagono(5, base)
    pentagono1.calcular_area()
    pentagono1.calcular_perimetro()
