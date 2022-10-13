
#para comenzar la suma declaramos los dos digitos que se van
# a sumar

sumafinal=[]
listaacarreo=[]

numero1=input("dame el primer numero: ")
longitudnumero1=len(numero1)
numero2=input("dame el segundo numero: ")
longitudnumero2=len(numero2)

#mientras sean de longitud diferente

while longitudnumero1!=longitudnumero2:

#hay que preguntarse a quien hay que acompletar

    if longitudnumero1>longitudnumero2:
        digitosfaltantes=longitudnumero1-longitudnumero2
        #en este caso hay que acompletar al numero 2
        numero2="0"+numero2
        longitudnumero2=longitudnumero2+1
    else:
        digitosfaltantes=longitudnumero2-longitudnumero1
        #en este caso hay que acompletar al numero 1
        numero1="0"+numero1
        longitudnumero1=longitudnumero1+1

#definimos a c como el acarreo
c=0

for i in range(1,longitudnumero1+1):

#obten los ultimos digitos
    a=numero1[-i]
    a=int(a)
    b=numero2[-i]
    b=int(b)

    if (a+b+c)>9:
        resultado=a+b+c
        resultado=resultado-10
        c=1
        print("el resultado es: ",resultado)
        print("el acarreo es: ",c)
        sumafinal.append(resultado)


    else:
        resultado=a+b+c
        c=0
        print("el resultado es: ",resultado)
        print("el acarreo es: ",c)
        sumafinal.append(resultado)

sumafinal.reverse()
listaacarreo.append(c)

if c==1:
    
    sumafinal=listaacarreo+sumafinal
    print("La suma final es: ",sumafinal)
else:
    print("La suma final es: ",sumafinal)
