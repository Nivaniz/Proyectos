import math

class Punto():

    # Constructor de clase
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # Método de clase para crear puntos fácilmente a partir de coordenadas
    @classmethod
    def crear_con_coordenadas(cls, coordenadas):
        if coordenadas:
            x, y = coordenadas
        else:
            x, y = 0, 0
        return cls(x, y)

    def __str__(self):  # Sobrescribimos el método para imprimir
        return "({},{})".format(self.x, self.y)

    # Método cuadrante que indique a que cuadrante pertenece el punto o si es origer
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está en el origen"
        elif self.x == 0:
            return "El punto está sobre el eje y"
        elif self.y == 0:
            return "El punto está sobre el eje x"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        else:
            return "El punto está en el cuarto cuadrante"

    # Método vector que tome otro punto y calcule el vector resultante entre dos puntos
    def vector(self, otro_punto):
        dx = otro_punto.x - self.x  # otro_punto = 3, self.x = 1
        dy = otro_punto.y - self.y  # otro_punto = 4, self.x = 2
        return Punto(dx, dy)  # (2,2)

    # Calcular la distancia entre dos puntos
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        return math.sqrt(dx ** 2 + dy ** 2)
        # Se utiliza para elevar al cuadrado los valores de dx y dy
        # antes de sumarlos y aplicar la raíz cuadrada
        # En resumen, dx**2 es equivalente a dx elevado al cuadrado


class Rectangulo():
    # Método para crear ambos puntos, si no se envian se crearán dos puntos en el origen por defecto
    def __init__(self, p1=None, p2=None):
        # Recibe dos argumentos opcionales p1 y p2. Si no se proporcionan
        # se crean dos objetos Punto con coordenadas (0,0)
        if p1 is None:
            p1 = Punto(0, 0)
        if p2 is None:
            p2 = Punto(0, 0)
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        #  se utiliza para imprimir los puntos que forman el rectángulo de forma legible.
        return f"[{self.p1}, {self.p2}]"

    def base(self):
        return abs(self.p1.x - self.p2.x)  # 0 - 3

    def altura(self):
        return abs(self.p1.y - self.p2.y)  # 0 - 4

    def area(self):
        return self.base() * self.altura()  # 3 * 4



print("--------Punto 0,0-----------")
p1 = Punto()
print(p1)  # imprime (0, 0)

print("--------Crea cordenadas------------")
p2 = Punto.crear_con_coordenadas((3, 4))
print(p2)  # imprime (3, 4)

print("--------Crea cordenadas 0,0------------")
p3 = Punto.crear_con_coordenadas((0, 0))
print(p3)  # imprime (0, 0)

print("------Conseguir el vector de dos puntos------------")
p4 = Punto(1, 2)
p5 = Punto(3, 4)
vec = p4.vector(p5)
print(vec)  # Imprime (2,2) el vector resultante

print("-------Conseguir la distancia entre dos puntos-------------")
distance = p4.distancia(p5)
print(distance)

print("-----Saber en que cuadrante está una coordenada--------")
print(p2.cuadrante())  # El punto está en el primer cuadrante

print("------Crear rectángulo con puntos nuevos---------")
# Crear un rectángulo con puntos en (0, 0) y (3, 4)
r1 = Rectangulo(Punto(0, 0), Punto(3, 4))
print(r1)  # Imprime: [(0,0), (3,4)]

# Crear un rectángulo con puntos por defecto en (0, 0)
r2 = Rectangulo()
print(r2)  # Imprime: [(0,0), (0,0)]


print("------Obtener la base, altura y area del rectángulo---------")
# Obtener la base del rectángulo
base = r1.base()
print(base)  # Imprime: 3

altura = r1.altura()
print(altura)  # Imprime: 4

# Obtener el área del rectángulo
area = r1.area()
print(area)  # Imprime: 12

print("Experimentación ")
A = Punto.crear_con_coordenadas((2, 3))
print(A)
B = Punto.crear_con_coordenadas((5, 6))
print(B)
C = Punto.crear_con_coordenadas((-3, -1))
print(C)
D = Punto.crear_con_coordenadas((0, 0))
print(D)

print("Pertenecen al cuadrante: ")
print(A.cuadrante())
print(C.cuadrante())
print(D.cuadrante())

print("Sus vectores son: ")
vecAB = A.vector(B)
print(vecAB)

vecBA = B.vector(A)
print(vecBA)

print("Su distancia es: ")
distan = A.distancia(B)
print(distan)

dista = B.distancia(A)
print(dista)

print("Más lejos del origen es: ")

din = A.distancia(p3)
print(din)

di = B.distancia(p3)
print(di)

d = C.distancia(p3)
print(d)

print("Crear un rectangulo utilizando puntos A Y B")
r2 = Rectangulo(A, B)
print(r2)

print("Base, altura y área del rectangulo: ")
base2 = r2.base()
print(base2)

altura2 = r2.altura()
print(altura2)

# Obtener el área del rectángulo
area2 = r2.area()
print(area2)