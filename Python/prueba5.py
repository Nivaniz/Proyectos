class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

nombres = ['Héctor', 'Mario', 'Marta']
personas = []

for n in nombres:
    p = Persona(n)
    personas.append(p)
    
print(n)
print(p)
