import os
import sys
from tabulate import tabulate
from math import pi

import numpy as np
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Poligono:
    def __init__(self):
        self.figuras = []
        self.data = []
        self.dibujar = []
        self.nodibujar = []
        self.resultados = []

    def rectangulo_add(self):
        """Rectangulo 1"""
        b = float(input(f"Ingresar el valor base la figura: "))
        h = float(input(f"Ingresar el valor altura la figura: "))
        x = float(input(f"Ingresa el desplazamiento en x: "))
        y = float(input(f"Ingresa el desplazamiento en y: "))

        while True:
            hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
            if hueco == "s" or hueco == "n":
                if hueco == 's':
                    hueco = True
                else:
                    hueco = False
                break

        area = h * b
        xp = b / 2
        yp = h / 2
        ix = (b * (h ** 3)) / 12
        iy = (h * (b ** 3)) / 12

        if hueco:
            rec = patches.Rectangle((x, y), b, h, fill=True)
            self.nodibujar.append(rec)
        else:
            rec = patches.Rectangle((x, y), b, h, fill=True)
            self.dibujar.append(rec)

        self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
        return [hueco, area, x, y, xp, yp, ix, iy]

    def triangulo_add(self):
        """Triangulo"""
        b = float(input(f"Ingresar el valor base la figura: "))
        h = float(input(f"Ingresar el valor altura la figura: "))
        a = float(input(f'Ingresar el valor de a: '))
        x = float(input(f"Ingresa el desplazamiento en x: "))
        y = float(input(f"Ingresa el desplazamiento en y: "))

        while True:
            hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
            if hueco == "s" or hueco == "n":
                if hueco == 's':
                    hueco = True
                else:
                    hueco = False
                break

        area = (b * h) / 2
        xp = (a + b) / 3
        yp = h / 3
        ix = (b * (h ** 3)) / 36
        iy = (b * h / 36) * ((a ** 2) - (a * b) + (b ** 2))

        if hueco:
            rec = triagulo(x, y, b, h, a)
            self.nodibujar.append(rec)
        else:
            rec = triagulo(x, y, b, h, a)
            self.dibujar.append(rec)

        self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
        return [hueco, area, x, y, xp + x, yp + y, ix, iy]

    def circulo_add(self, tipo):
        if tipo == 1:
            """Completo"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2)
            xp = 0
            yp = 0
            ix = (pi * (r ** 4)) / 4
            iy = (pi * (r ** 4)) / 4

            if hueco:
                rec = patches.Circle((x, y), r, fill=True)
                self.nodibujar.append(rec)
            else:
                rec = patches.Circle((x, y), r, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 2:
            """Semiciculo superior"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 2
            xp = 0
            yp = 4 * r / (3 * pi)
            ix = 0.1098 * (r ** 4)
            iy = (r ** 4) * pi / 8

            if hueco:
                rec = patches.Wedge([x, y], r, 0, 180, fill=True)
                self.nodibujar.append(rec)
            else:
                rec = patches.Wedge([x, y], r, 0, 180, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 3:
            """Semiciculo derecha"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 2
            xp = (4 * r) / (3 * pi)
            yp = 0
            ix = (r ** 4) * pi / 8
            iy = 0.1098 * (r ** 4)

            if hueco:
                rec= patches.Wedge([x, y], r, 0, 180, fill=True, color='#white')
                self.nodibujar.append(rec)
            else:
                rec= patches.Wedge([x, y], r, -90, 90, fill=True, color='#00AAE4')
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 4:
            """Semiciculo inferior"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 2
            xp = (-4 * r) / (3 * pi)
            yp = 0
            ix = 0.1098 * (r ** 4)
            iy = (r ** 4) * pi / 8

            if hueco:
                rec= patches.Wedge([x, y], r, 180, 360, fill=True)
                self.nodibujar.append(rec)
            else:
                rec= patches.Wedge([x, y], r, 180, 360, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 5:
            """Semiciculo izquierda"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 2
            xp = (-4 * r) / (3 * pi)
            yp = 0
            ix = (r ** 4) * pi / 8
            iy = 0.1098 * (r ** 4)

            if hueco:
                rec = patches.Wedge([x, y], r, 90, 270, fill=True)
                self.nodibujar.append(rec)
            else:
                rec = patches.Wedge([x, y], r, 90, 270, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 6:
            """Cuarto I"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 4
            xp = (4 * r) / (3 * pi)
            yp = (4 * r) / (3 * pi)
            ix = (r ** 4) * ((pi / 16) - (4 / (9 * pi)))
            iy = 0.05487 * (r ** 4)

            if hueco:
                rec= patches.Wedge([x, y], r, 0, 90, fill=True)
                self.nodibujar.append(rec)
            else:
                rec= patches.Wedge([x, y], r, 0, 90, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 7:
            """Cuarto II"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 4
            xp = (-4 * r) / (3 * pi)
            yp = (4 * r) / (3 * pi)
            ix = (r ** 4) * ((pi / 16) - (4 / (9 * pi)))
            iy = 0.05487 * (r ** 4)

            if hueco:
                rec= patches.Wedge([x, y], r, 90, 180, fill=True)
                self.nodibujar.append(rec)
            else:
                rec= patches.Wedge([x, y], r, 90, 180, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 8:
            """Cuarto III"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 4
            xp = (-4 * r) / (3 * pi)
            yp = (-4 * r) / (3 * pi)
            ix = (r ** 4) * ((pi / 16) - (4 / (9 * pi)))
            iy = 0.05487 * (r ** 4)

            if hueco:
                rec= patches.Wedge([x, y], r, 180, 270, fill=True)
                self.nodibujar.append(rec)
            else:
                rec= patches.Wedge([x, y], r, 180, 270, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        if tipo == 9:
            """Cuarto IV"""
            r = float(input(f"Ingresar el valor radio la figura: "))
            x = float(input(f"Ingresa el desplazamiento en x: "))
            y = float(input(f"Ingresa el desplazamiento en y: "))

            while True:
                hueco = input(f"¿Esta figura es un hueco? (s/n): ").lower()
                if hueco == "s" or hueco == "n":
                    if hueco == 's':
                        hueco = True
                    else:
                        hueco = False
                    break

            area = pi * (r ** 2) / 4
            xp = (4 * r) / (3 * pi)
            yp = (-4 * r) / (3 * pi)
            ix = (r ** 4) * ((pi / 16) - (4 / (9 * pi)))
            iy = 0.05487 * (r ** 4)

            if hueco:
                rec = patches.Wedge([x, y], r, 270, 360, fill=True)
                self.nodibujar.append(rec)
            else:
                rec = patches.Wedge([x, y], r, 270, 360, fill=True)
                self.dibujar.append(rec)

            self.figuras.append([hueco, area, x, y, xp + x, yp + y, ix, iy])
            return [hueco, area, x, y, xp, yp, ix, iy]
        else:
            print(f'El valor no esta dentro de la lista')
            pass

    def calcular_centroide(self):
        suma_area = 0
        suma_ax = 0
        suma_ay = 0
        self.data = []
        headers = ['No Figura',
                   'Area [u²]',
                   'Xi [u]',
                   'Yi [u]',
                   'A*Xi [u³]',
                   'A*Yi [u³]',
                   "Ix' [u]",
                   "Iy' [u]",
                   "Dx [u]",
                   'Dy [u]',
                   'Ixc[u⁴]',
                   'Iyc[u⁴]']
        for figura in self.figuras:
            aux = [0] * 11
            # [hueco, area, x, y, xp, yp, ix, iy]
            if figura[0]:
                aux[0] = -1 * figura[1]
                aux[5] = -1 * figura[6]
                aux[6] = -1 * figura[7]

            else:
                aux[0] = figura[1]
                aux[5] = figura[6]
                aux[6] = figura[7]

            aux[1] = figura[4]          # Xi
            aux[2] = figura[5]          # Yi
            aux[3] = aux[0] * aux[1]    # Axi
            aux[4] = aux[0] * aux[2]    # Ayi
            aux[5] = figura[6]          # I'x
            aux[6] = figura[7]          # I'y

            suma_area = suma_area + aux[0]
            suma_ax = suma_ax + aux[3]
            suma_ay = suma_ay + aux[4]

            self.data.append(aux)
        Cx = suma_ax/suma_area
        Cy = suma_ay/suma_area

        sumaix = 0
        sumaiy = 0

        for figura in self.data:
            print(Cx - figura[1])
            print(figura)
            self.data[self.data.index(figura)][7] = (Cx - figura[1])                          # Dx
            self.data[self.data.index(figura)][8] = (Cy - figura[2])                          # Dy
            print(figura)
            self.data[self.data.index(figura)][9] = figura[5] + (figura[0] * (figura[8] ** 2))     # Ixc
            self.data[self.data.index(figura)][10] = figura[6] + (figura[0] * (figura[7] ** 2))     # Iyc
            if (figura[0]/figura[0]) == -1:
                figura[9] = -figura[9]
                figura[10] = -figura[10]

            sumaiy = sumaiy + figura[10]
            sumaix = sumaix + figura[9]

        a = f"\n\nEl centroide de la figura se ubica en:\n" \
            f"\tPx = {Cx}\n" \
            f"\tPy = {Cy}"
        print(a)
        a = f"\n\nEL resutado de la inercia es: \n" \
            f"\tIx = {sumaix}\n" \
            f"\tIy = {sumaiy}"
        print(a)

        rec = patches.Circle((Cx, Cy), 0.25, fill=True)
        self.resultados.append(rec)
        self.resultados.append(rec)

        tabla = tabulate(self.data, headers=headers, showindex=True)
        print(tabla)

        with open("tabla.txt", 'w') as f:
            f.write(tabla)
            a = f"\n\nEl centroide de la figura se ubica en:\n" \
                f"\tPx = {Cx}\n" \
                f"\tPy = {Cy}"
            f.write(a)
            a = f"\n\nEL resutado de la inercia es: \n" \
                f"\tIx = {sumaix}\n" \
                f"\tIy = {sumaiy}"
            f.write(a)
            f.write("\n\nGracias por usar")
            f.write("\n\nFI - UAEMex, 2021")


    def eliminar_figura(self):
        headers = ['No Figura',
                   'Hueco',
                   'X [u]',
                   'Y [u]',
                   'Xp [u]',
                   'Yp [u]',
                   "Ix' [u]",
                   "Iy' [u]"]

        print(tabulate(self.figuras, headers=headers, showindex=True))

        print('¿Qué columa quieres eliminar?')
        sel = int(input('>> '))
        self.figuras.pop(sel)
        self.dibujar.pop(sel)


    def dibujar_figura(self):
        fig, ax = plt.subplots()
        p = PatchCollection(self.dibujar, alpha=0.4, facecolors= 'green')
        d = PatchCollection(self.nodibujar, alpha=0.4, facecolors='white')
        q = PatchCollection(self.resultados, alpha=0.4, facecolors='red')
        ax.add_collection(p)
        ax.add_collection(d)
        ax.add_collection(q)
        ax.set_title('Centroide de la figura')
        plt.grid()
        plt.xlabel("x [u]")
        plt.ylabel("y [u]")
        plt.autoscale()
        plt.savefig('Figura.png')
        plt.show()

def triagulo(x, y, b, h, a):
    pol1 = patches.Polygon(np.array([[x, y], [x + a, y + h], [x + b, y]]))
    return pol1



def borrar_pantalla():          # Definimos la función estableciendo el nombre que queramos
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


def mostrar_figuras():
    figuras = ['Rectangulo', 'Triangulo', 'Circulo']
    print(f"¿Qué figura deseas agregar? (Seleccionar un numero)")
    for figura in figuras:
        print(f"{figuras.index(figura) + 1}.- {figura}")


def mostar_circulos():
    figuras = ['Completo', 'Medio circulo superior', 'Medio circulo derecha',
               'Medio circulo inferior', 'Medio circulo izquierda',
               'Cuarto circulo I', 'Cuarto circulo II', 'Cuarto circulo III', 'Cuarto circulo IV']
    print(f"¿Qué figura deseas agregar? (Seleccionar un numero)")
    for figura in figuras:
        print(f"{figuras.index(figura) + 1}.- {figura}")


def mensaje():
    txt = f"1. Agregar una figura \n" \
          f"2. Eliminar alguna figura\n" \
          f"3. Calcular \n" \
          f"salir"
    print(txt)


if __name__ == '__main__':
    f_geomtricas = ['Rectangulo', 'Triangulo', 'Circulo']
    p = Poligono()
    borrar_pantalla()
    print("//---SOFTWARE DESARROLLADO POR ALEJANDRO BRACAMONTE---//")
    print("Bienvenido, ¿Que es lo que quieres hacer?")
    while True:
        borrar_pantalla()
        mensaje()
        selector = input('>> ').lower()
        if selector == 'salir':
            break
        if selector == '1':             # Agregar figura
            borrar_pantalla()
            mostrar_figuras()
            sel_figure = input('>> ').lower()
            if sel_figure == '1':         # Rectangulo
                borrar_pantalla()
                p.rectangulo_add()
            if sel_figure == '2':         # Triangulo
                borrar_pantalla()
                p.triangulo_add()
            if sel_figure == '3':         # Circulos
                borrar_pantalla()
                mostar_circulos()
                selector = int(input('>> '))
                borrar_pantalla()
                p.circulo_add(selector)

        if selector == '2':         # Eliminar una figura
            borrar_pantalla()
            p.eliminar_figura()
        if selector == '3':         # Realizar Calculos
            borrar_pantalla()
            p.calcular_centroide()
            p.dibujar_figura()
            quit()
