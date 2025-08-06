inicio = 0
limite = 0
print("Programa que imprime los números pares entre dos números dados")
inicio = int(input("Ingrese el valor de inicio: "))
limite = int(input("Ahora el valor de fin: "))
for x in range(inicio, limite):
    if x % 2 == 0 :
        print(f"| {x}", end=" ")
