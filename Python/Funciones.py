def doblar(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])
        
    
doblar(n=5, c="Hola")

def factorial(num):
    if num > 1:
        num = num * factorial(num -1)
    return num

print(factorial(5))

# Completa el ejercicio
def sumatorio(numero):
    if numero > 1:
        numero = numero +sumatorio(numero -1)
    return numero

print(sumatorio(5))

