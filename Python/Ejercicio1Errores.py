def dividir(a, b):
    try:
        return a/b
    except:
        if b == 0:
            print("No se puede dividir entre cero")
    
    
print(dividir(0,0))

