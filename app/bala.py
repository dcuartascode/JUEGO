import pygame

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad_y = -5  # Velocidad de la bala (negativa para que suba)
        self.rect = pygame.Rect(x, y, 5, 5)  # Rectángulo para manejar colisiones

    def mover(self):
        self.y += self.velocidad_y  # Actualizamos la posición vertical
        self.rect.y = self.y  # Actualizamos la posición del rectángulo
