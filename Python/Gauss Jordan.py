#Programa que resuelve sistemas de ecuaciones de 3x3
print("Ingrese la primera ecuacion")
print("Debe ingresar el valor de x, y, z y r")
print("x -> primer valor")
print("y -> segundo valor")
print("z -> tercer valor")
print("r -> resultado")

#Pedimos los datos de la ecuacion al usuario
def pedirEcuacion():
    print("Ingrese los valores de la ecuacion")
    ec=[]
    for i in range(4):
        valor=int(input("Ingrese el valor > "))
        ec.append(valor)
    return ec

#Declaramos las tres ecuaciones
ec1=pedirEcuacion()
print("")
ec2=pedirEcuacion()
print("")
ec3=pedirEcuacion()

#Dividir la ec/ec[0] para obtener 1
def obtenerUno(ecuacion):
    for i in range(4):
        nvalor=ecuacion[i]/ecuacion[0]
        ecuacion.append(nvalor)
    return ecuacion

nec1=obtenerUno(ec1)

del nec1[0:4]

#Convertimos en cero las demas filas con el primer pivote
def primerPivoteDos(nec1, ec2):
    #Multiplicamos el pivote por -(ecuacion[0]) y le sumamos ecuacion[0]
    for i in range(4):
        nvalor=(nec1[i]*-(ec2[0]))+ec2[i]
        ec2.append(nvalor)
    return ec2

def primerPivoteTres(nec1, ec3):
    #Multiplicamos el pivote por -(ecuacion[0]) y le sumamos ecuacion[0]
    for i in range(4):
        nvalor=(nec1[i]*-(ec3[0]))+ec3[i]
        ec3.append(nvalor)
    return ec3

ec2=primerPivoteDos(nec1, ec2)
ec3=primerPivoteTres(nec1, ec3)

del ec2[0:4]
del ec3[0:4]

#Dividir la ec/ec[1] para obtener 1
def obtenerUno2(ecuacion):
    for i in range(4):
        nvalor=ecuacion[i]/ecuacion[1]
        ecuacion.append(nvalor)
    return ecuacion 

nec2=obtenerUno2(ec2)
del nec2[0:4]

#Convertimos en cero las demas filas con el segundo pivote
def segundoPivoteUno(nec1, nec2):
    for i in range(4):
        nvalor=(nec2[i]*-(nec1[1]))+nec1[i]
        nec1.append(nvalor)
    return nec1

def segundoPivoteTres(ec3, nec2):
    for i in range(4):
        nvalor=(nec2[i]*-(ec3[1]))+ec3[i]
        ec3.append(nvalor)
    return ec3

nec1=segundoPivoteUno(nec1, nec2)
ec3=segundoPivoteTres(ec3, nec2)
del nec1[0:4]
del ec3[0:4]

#Dividir la ec/ec[2] para obtener 1
def ObtenerUno3(ecuacion):
    for i in range(4):
        nvalor=ecuacion[i]/ecuacion[2]
        ecuacion.append(nvalor)
    return ecuacion

nec3=ObtenerUno3(ec3)
del nec3[0:4]

#Convertimos en cero las demas filas con el tercer pivote
def tercerPivoteUno(nec1, nec3):
    for i in range(4):
        nvalor=(nec3[i]*-(nec1[2]))+nec1[i]
        nec1.append(nvalor)
    return nec1

def tercerPivoteDos(nec2, nec3):
    for i in range(4):
        nvalor=(nec3[i]*-(nec2[2]))+nec2[i]
        nec2.append(nvalor)
    return nec2

nec1=tercerPivoteUno(nec1, nec3)
nec2=tercerPivoteDos(nec2, nec3)
del nec1[0:4]
del nec2[0:4]

print("")
print("RESULTADOS")
print(nec1, "\n", nec2, "\n", nec3, "\n")
print("x -> ", nec1[3], "\ny -> ", nec2[3], "\nz -> ", nec3[3])