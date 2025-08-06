lista = []
def cargarContenido(dato):
    lista.append(dato)

def imprimirLista():
    print(lista)

def quitarDeLista(dato):
    lista.remove(dato)

if __name__ == "__main__":
    cargarContenido("REGINA")
    cargarContenido("BARRETO")
    imprimirLista()
    quitarDeLista("REGINA")
    imprimirLista()