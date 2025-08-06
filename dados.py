import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la pantalla
ANCHO, ALTO = 700, 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Dados 🎲")

# Fuente para texto
fuente = pygame.font.SysFont(None, 40)

# Coordenadas relativas para los puntos del dado (en una cuadrícula 3x3)
posiciones_puntos = {
    1: [(1, 1)],
    2: [(0, 0), (2, 2)],
    3: [(0, 0), (1, 1), (2, 2)],
    4: [(0, 0), (0, 2), (2, 0), (2, 2)],
    5: [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)],
    6: [(0, 0), (1, 0), (2, 0), (0, 2), (1, 2), (2, 2)],
}

def dibujar_dado(x, y, valor, tam=100):
    pygame.draw.rect(pantalla, NEGRO, (x, y, tam, tam), border_radius=15)
    pygame.draw.rect(pantalla, BLANCO, (x+5, y+5, tam-10, tam-10), border_radius=10)

    radio = 8
    offset = tam // 4
    for fila, col in posiciones_puntos[valor]:
        cx = x + offset * (col + 1)
        cy = y + offset * (fila + 1)
        pygame.draw.circle(pantalla, NEGRO, (cx, cy), radio)

def lanzar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def dibujar_pantalla(d1, d2):
    pantalla.fill(BLANCO)
    
    texto = fuente.render("Haz clic o pulsa una tecla para tirar los dados", True, NEGRO)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 20))

    # Dibujar dados
    dibujar_dado(ANCHO // 4 - 50, ALTO // 2 - 50, d1)
    dibujar_dado(3 * ANCHO // 4 - 50, ALTO // 2 - 50, d2)

    suma = d1 + d2
    texto_suma = fuente.render(f"Suma: {suma}", True, NEGRO)
    pantalla.blit(texto_suma, (ANCHO // 2 - texto_suma.get_width() // 2, ALTO - 50))

    pygame.display.flip()

def main():
    d1, d2 = lanzar_dados()
    dibujar_pantalla(d1, d2)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN or evento.type == pygame.KEYDOWN:
                d1, d2 = lanzar_dados()
                dibujar_pantalla(d1, d2)

main()
