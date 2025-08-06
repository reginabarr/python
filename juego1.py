import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 500, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("La Viborita")

# Colores
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Tamaño de cada segmento de la serpiente y comida
SIZE = 20

# FPS
clock = pygame.time.Clock()
FPS = 10

# Fuente para mostrar puntuación
font = pygame.font.SysFont(None, 30)

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(window, GREEN, pygame.Rect(segment[0], segment[1], SIZE, SIZE))

def draw_food(food_pos):
    pygame.draw.rect(window, RED, pygame.Rect(food_pos[0], food_pos[1], SIZE, SIZE))

def show_score(score):
    text = font.render(f"Puntuación: {score}", True, (255, 255, 255))
    window.blit(text, (10, 10))

def main():
    # Posición inicial de la serpiente (x, y)
    snake_pos = [100, 100]
    # Cuerpo de la serpiente: lista con segmentos
    snake_body = [[100, 100]]

    # Posición inicial de la comida
    food_pos = [random.randrange(0, WIDTH - SIZE, SIZE), random.randrange(0, HEIGHT - SIZE, SIZE)]

    # Dirección inicial: mover a la derecha
    direction = "RIGHT"
    change_to = direction

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Captura teclas de dirección
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        direction = change_to

        # Mover la serpiente
        if direction == "UP":
            snake_pos[1] -= SIZE
        elif direction == "DOWN":
            snake_pos[1] += SIZE
        elif direction == "LEFT":
            snake_pos[0] -= SIZE
        elif direction == "RIGHT":
            snake_pos[0] += SIZE

        # Insertar nueva posición al inicio del cuerpo (cabeza)
        snake_body.insert(0, list(snake_pos))

        # Verificar si la serpiente come la comida
        if snake_pos == food_pos:
            score += 1
            # Generar nueva comida en posición aleatoria
            food_pos = [random.randrange(0, WIDTH - SIZE, SIZE), random.randrange(0, HEIGHT - SIZE, SIZE)]
        else:
            # Quitar el último segmento si no comió
            snake_body.pop()

        # Rellenar la ventana de negro
        window.fill(BLACK)

        # Dibujar comida y serpiente
        draw_food(food_pos)
        draw_snake(snake_body)
        show_score(score)

        # Condiciones para que el juego termine (chocar con bordes o con el cuerpo)
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            running = False

        # Verificar choque con el cuerpo
        for block in snake_body[1:]:
            if snake_pos == block:
                running = False

        pygame.display.update()
        clock.tick(FPS)

    # Fin del juego
    pygame.quit()

if __name__ == "__main__":
    main()
