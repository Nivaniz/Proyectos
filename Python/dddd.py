class Point:
    def __init__(self, x, y):  # CONSTRUCTOR DE OBJETOS
        self.x = x  # referenciamos el objeto actual, ponemos el atributo a con el argumento a a la funcion def
        self.y = y  # self es una referencia al objeto y lo asignamos

    def move(self):
        print("move")

    def draw(self):
        print("draw")

# Constructores
point = Point(10,20)
print(point.x)  # Imprime 10

# instanciamos una clase
# Creamos un objeto y lo guardamos en una variable
point1 = Point()  # Objeto 1 con una clase agregada como funcion
point1.x = 10  # Agregamos atributos
point1.y = 20
print(point1.x) # imprimimos atributos
point1.draw()