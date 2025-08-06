#Desarrollado por Regina Barreto
edad = int(input("Ingrese su edad: "))

print(f"Usted tiene {edad} años" )

if edad >= 18 and edad < 60:
    print("Usted es mayor de edad. Licencia de adulto")
elif edad < 18 and edad >= 16:
    print("Usted es menor de edad. Licencia de menor")
else:
    print("Usted no puede tener licencia de conducir")
    print("Vuelva dentro de ??? años.")
