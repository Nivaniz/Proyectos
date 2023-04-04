def agregar(lista,text):
    try:
        if text in lista:
            raise ValueError
        else:
            lista.append(text)
        return lista
    except ValueError:
         print("no se puede aladir elementos duplicados -> {}".format(text))
    
    
        
text = [2, 3, 5, 6]

print(agregar(text,20))
print(agregar(text,5))
print(agregar(text,8))