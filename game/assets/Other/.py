import pygame

pygame.init()

# Carga la imagen original
imagen_original = pygame.image.load("game/assets/Other/Reset.png")

# Define el tamaño del borde y el color
borde_ancho = 5
borde_color = (255, 0, 0)  # Rojo (R, G, B)

# Calcula las dimensiones de la imagen con el borde
ancho_nuevo = imagen_original.get_width() + borde_ancho * 2
alto_nuevo = imagen_original.get_height() + borde_ancho * 2

# Crea una nueva superficie del tamaño del borde
superficie_borde = pygame.Surface((ancho_nuevo, alto_nuevo))

# Dibuja la imagen original en la superficie del borde, ajustando la posición
superficie_borde.blit(imagen_original, (borde_ancho, borde_ancho))

# Dibuja un rectángulo alrededor de la imagen en la superficie del borde
pygame.draw.rect(superficie_borde, borde_color, pygame.Rect(0, 0, ancho_nuevo, alto_nuevo), borde_ancho)

# Crea una ventana para mostrar la imagen con borde
screen = pygame.display.set_mode((ancho_nuevo, alto_nuevo))
pygame.display.set_caption("Imagen con Borde")

# Dibuja la superficie del borde en la ventana
screen.blit(superficie_borde, (0, 0))
pygame.display.flip()

# Espera a que se cierre la ventana
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
