import random

# Lista de palabras para adivinar
palabras = ["python", "computadora", "programacion", "juego", "teclado", "pantalla", "internet"]

# Elegir una palabra aleatoria
palabra_oculta = random.choice(palabras)
palabra_mostrada = ["_"] * len(palabra_oculta)

intentos_maximos = 6
letras_adivinadas = []
intentos_fallidos = 0

print("¡Bienvenido al juego del Ahorcado!")
print("Tienes que adivinar la palabra antes de quedarte sin intentos.")

# Juego principal
while intentos_fallidos < intentos_maximos and "_" in palabra_mostrada:
    print("\nPalabra:", " ".join(palabra_mostrada))
    print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")
    print(f"Intentos restantes: {intentos_maximos - intentos_fallidos}")
    
    letra = input("Adivina una letra: ").lower()
    
    if not letra.isalpha() or len(letra) != 1:
        print("Por favor, ingresa una sola letra válida.")
        continue

    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra. Intenta con otra.")
        continue

    letras_adivinadas.append(letra)

    if letra in palabra_oculta:
        print("¡Bien hecho! La letra está en la palabra.")
        for i, l in enumerate(palabra_oculta):
            if l == letra:
                palabra_mostrada[i] = letra
    else:
        print("Lo siento, esa letra no está en la palabra.")
        intentos_fallidos += 1

# Resultado final
if "_" not in palabra_mostrada:
    print("\n¡Felicidades! Adivinaste la palabra:", palabra_oculta)
else:
    print("\nTe has quedado sin intentos. La palabra era:", palabra_oculta)
