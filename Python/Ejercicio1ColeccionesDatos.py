# Crea conjunto con usuarios y admin
usuarios = {'Marta', 'David', 'Elvira', 'Juan', 'Marcos'}
administradores = {'Juan', 'Maria'}

# Borra al administrador juan del conjunto
administradores.discard('Juan')

# Añade a Marcos como nuevo admin pero no se borra de usuarios
administradores.add('Marcos')

# Muestra todos los usuarios y decir si es usuario o admin

for persona in usuarios:
    if persona in administradores:
        print(persona + " esta en admin y usuario")
        save = persona
    else:
        print(persona + " es usuario")
    
for persona in administradores:
    if save == persona in administradores:
        continue
    else:
        print(persona + " es admin")