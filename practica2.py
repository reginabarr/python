diccUsuario = {"admin":"12345", "moises":"abcd"}

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

intentos = 0
if user in diccUsuario:
    #usuario existente
    intentos = intentos + 1
    while intentos < 3:
        if password == diccUsuario[user]:
            print("Acceso correto")
            break
        else: 
            print("Acceso incorrecto")
            intentos = intentos + 1
            password = input(f"Intento {intentos} de 3. Reescriba su contraseña: ")
else:
    print("Usuario no registrado")        
