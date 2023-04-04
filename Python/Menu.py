num1 = 0
num2 = 0
texto = ''


class Operaciones:      
    def sumar(self, num1, num2):
        resultado = num1 + num2
        return resultado
    
    def resta(self, num1, num2):
        resultado = num1 - num2
        return resultado
    
    def multiplicacion(self, num1, num2):
        resultado = num1 * num2
        return resultado


muestra = Operaciones()

while True:
    num1 = int(input("Dame el primer numero"))
    num2 = int(input("Dame el segundo numero"))
    texto = input("Seleccione una opción: 1) SUMA 1 2) RESTA 2 3) MULTIPLICACION 4) EXIT  ")
    
    if texto == "S":
        print(muestra.sumar(num1,num2))
    elif texto == "R":
        print(muestra.resta(num1,num2))
    elif texto == "M":
        print(muestra.multiplicacion(num1,num2))
    elif texto == 'SA':
        break
    else:
        print("Opción invalida")
      
    
