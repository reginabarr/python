import time
import os
traductorSpEn = {"hola":"hello", "adiós":"bye"}

while True:
    palabra = input("Traducir: ")

    if palabra != "0":
        if palabra in traductorSpEn:
            print(f"Español\t|\tIngles")
            print(f"{palabra}\t|\t{traductorSpEn[palabra]}")
        else:
            print("No se encuentra en el diccionario")
            resp = input("Desea agregarlo (s/n)")

            if resp == "s":
                traduccion = input(f"Ingrese la traducción de {palabra}: ")
                if len(traduccion) > 0:
                    traductorSpEn[palabra] = traduccion
                    print("Agregado al diccionario.")
                    time.sleep(2)
                    os.system("cls")

    else:
        break

         