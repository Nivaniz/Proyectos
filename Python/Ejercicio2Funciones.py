def pares(lista):
    par_list = []
    impar_list = []
    lista.sort()
    
    for num in lista:
      if num % 2 == 0:
          par_list.append(num)
      else:
           impar_list.append(num)
    return par_list, impar_list
    


lista = [2, 4, 5, 3]
print(pares(lista))